"""Chapter 18 (Listings 18.1-18.5) -- A PyQt6 front end for a 1-D transient
conduction solver: parameter form, a Run button, a background worker thread so
the window stays responsive, and an embedded live Matplotlib plot.

Requires: PyQt6, matplotlib, numpy.
Run:  python solver_gui.py

Python for Engineers and Scientists, Chapter 18.
"""

from __future__ import annotations

import sys

import numpy as np
from PyQt6.QtCore import QObject, QThread, pyqtSignal
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout,
    QDoubleSpinBox, QSpinBox, QPushButton, QLabel, QProgressBar,
)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class SolverWorker(QObject):
    """Runs the solver off the GUI thread, reporting via signals."""

    progress = pyqtSignal(int)
    finished = pyqtSignal(np.ndarray, np.ndarray)

    def __init__(self, alpha: float, n_cells: int, n_steps: int) -> None:
        super().__init__()
        self.alpha, self.n_cells, self.n_steps = alpha, n_cells, n_steps

    def run(self) -> None:
        x = np.linspace(0.0, 1.0, self.n_cells)
        dx = x[1] - x[0]
        dt = 0.4 * dx**2 / self.alpha
        T = np.exp(-200.0 * (x - 0.5) ** 2)
        r = self.alpha * dt / dx**2
        for step in range(self.n_steps):
            T[1:-1] += r * (T[2:] - 2.0 * T[1:-1] + T[:-2])
            if step % (self.n_steps // 100 or 1) == 0:
                self.progress.emit(int(100 * step / self.n_steps))
        self.finished.emit(x, T)


class PlotCanvas(FigureCanvasQTAgg):
    """A Matplotlib canvas embedded as a Qt widget."""

    def __init__(self) -> None:
        self.figure = Figure(figsize=(5, 3))
        self.ax = self.figure.add_subplot(111)
        super().__init__(self.figure)

    def show_field(self, x, T) -> None:
        self.ax.clear()
        self.ax.plot(x, T)
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("T")
        self.draw()


class SolverWindow(QMainWindow):
    """The main window: parameter form, run button, progress, and plot."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Heat Conduction Solver")

        form = QFormLayout()
        self.alpha = QDoubleSpinBox()
        self.alpha.setRange(1e-7, 1e-3)
        self.alpha.setDecimals(7)
        self.alpha.setValue(1e-5)
        self.n_cells = QSpinBox()
        self.n_cells.setRange(8, 2000)
        self.n_cells.setValue(201)
        form.addRow("Diffusivity alpha (m^2/s):", self.alpha)
        form.addRow("Number of cells:", self.n_cells)

        self.run_button = QPushButton("Run")
        self.progress = QProgressBar()
        self.status = QLabel("ready")
        self.canvas = PlotCanvas()

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.run_button)
        layout.addWidget(self.progress)
        layout.addWidget(self.status)
        layout.addWidget(self.canvas)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

        self.run_button.clicked.connect(self.on_run)

    def on_run(self) -> None:
        self.thread = QThread()
        self.worker = SolverWorker(self.alpha.value(), self.n_cells.value(),
                                   n_steps=20_000)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.progress.connect(self.progress.setValue)
        self.worker.finished.connect(self.on_finished)
        self.worker.finished.connect(self.thread.quit)
        self.run_button.setEnabled(False)
        self.status.setText("running ...")
        self.thread.start()

    def on_finished(self, x: np.ndarray, field: np.ndarray) -> None:
        self.status.setText(f"done: peak T = {field.max():.4f}")
        self.canvas.show_field(x, field)
        self.run_button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SolverWindow()
    window.show()
    sys.exit(app.exec())

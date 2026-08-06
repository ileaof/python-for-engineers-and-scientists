"""Listing 6.2 -- The shared plotting module.

Consistent, publication-quality plotting helpers. Every figure in the book uses
the same restrained, colour-blind-friendly palette and layout conventions.
Collecting them here keeps the look uniform. Adapted from the Statistical
Thermodynamics package.

Python for Engineers and Scientists, Chapter 6.
Import:  from plotting import new_figure, apply_style, COLORS
"""

from __future__ import annotations

import matplotlib
import matplotlib.pyplot as plt

# Named colours used consistently; legible in grayscale.
COLORS = {
    "navy": "#2c3e50",       # primary data / reference curves
    "red": "#c0392b",        # highlighted result / exact value
    "blue": "#2980b9",       # secondary series
    "green": "#27ae60",      # limits / annotations
    "orange": "#e67e22",     # tertiary series
    "grey": "#95a5a6",       # de-emphasised guides
}
CYCLE = [COLORS["navy"], COLORS["red"], COLORS["blue"],
         COLORS["green"], COLORS["orange"], COLORS["grey"]]


def apply_style() -> None:
    """Apply the book's global Matplotlib style. Safe to call repeatedly."""
    matplotlib.rcParams.update({
        "figure.dpi": 110,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "font.size": 11,
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "axes.prop_cycle": matplotlib.cycler(color=CYCLE),
        "legend.frameon": False,
        "lines.linewidth": 2.0,
        "figure.constrained_layout.use": True,
    })


def new_figure(nrows: int = 1, ncols: int = 1, figsize=None):
    """Create a styled figure and axes, as plt.subplots would return."""
    apply_style()
    if figsize is None:
        figsize = (5.5 * ncols, 4.0 * nrows)
    return plt.subplots(nrows, ncols, figsize=figsize)

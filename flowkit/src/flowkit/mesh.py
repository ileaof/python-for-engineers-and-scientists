"""Structured 2-D grid for the cavity solver."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True, slots=True)
class UniformGrid2D:
    """A uniform (n+1) x (n+1) node grid on the unit square [0, 1]^2."""

    n: int

    @property
    def h(self) -> float:
        """Grid spacing."""
        return 1.0 / self.n

    @property
    def coordinates(self) -> tuple[np.ndarray, np.ndarray]:
        """1-D coordinate arrays (x, y) of the nodes."""
        c = np.linspace(0.0, 1.0, self.n + 1)
        return c, c

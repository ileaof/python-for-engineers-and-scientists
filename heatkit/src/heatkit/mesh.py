"""1-D radial finite-volume mesh (planar/cylindrical/spherical)."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True, slots=True)
class RadialMesh:
    """Uniform 1-D mesh on [r0, r1] with n cells."""

    r0: float
    r1: float
    n: int

    @property
    def faces(self) -> np.ndarray:
        """The n + 1 cell-face radii."""
        return np.linspace(self.r0, self.r1, self.n + 1)

    @property
    def centers(self) -> np.ndarray:
        """The n cell-centre radii."""
        f = self.faces
        return 0.5 * (f[:-1] + f[1:])

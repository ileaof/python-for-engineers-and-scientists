"""Listing 3.4 -- A 1-D finite-volume mesh as a dataclass whose geometry is
exposed as NumPy arrays.

Python for Engineers and Scientists, Chapter 3.
Run:  python listing_3_4_mesh1d.py
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True, slots=True)
class Mesh1D:
    """Uniform 1-D finite-volume mesh on the interval [0, L]."""

    length: float
    n_cells: int

    @property
    def dx(self) -> float:
        """Uniform cell width, in metres."""
        return self.length / self.n_cells

    @property
    def x_faces(self) -> np.ndarray:
        """Coordinates of the n_cells + 1 cell faces."""
        return np.linspace(0.0, self.length, self.n_cells + 1)

    @property
    def x_centers(self) -> np.ndarray:
        """Coordinates of the n_cells cell centres."""
        faces = self.x_faces
        return 0.5 * (faces[:-1] + faces[1:])


if __name__ == "__main__":
    mesh = Mesh1D(length=1.0, n_cells=8)
    print("dx       =", mesh.dx)
    print("faces    =", mesh.x_faces)
    print("centers  =", mesh.x_centers)

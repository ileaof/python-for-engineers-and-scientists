"""Streamfunction Poisson solver (Chapter 22)."""

from __future__ import annotations

import numpy as np


def solve_streamfunction(psi: np.ndarray, omega: np.ndarray, h: float,
                         n_sweeps: int = 15) -> np.ndarray:
    """Advance Laplacian(psi) = -omega by n_sweeps Jacobi/SOR sweeps.

    Interior update only; boundary psi is held fixed (no-through-flow walls).
    A few sweeps per outer iteration suffice, because the outer loop re-solves
    this as the vorticity field evolves.
    """
    for _ in range(n_sweeps):
        psi[1:-1, 1:-1] = 0.25 * (
            psi[2:, 1:-1] + psi[:-2, 1:-1] +
            psi[1:-1, 2:] + psi[1:-1, :-2] +
            h * h * omega[1:-1, 1:-1]
        )
    return psi

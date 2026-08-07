"""Unconditionally stable implicit transient conduction (Chapter 23)."""

from __future__ import annotations

import numpy as np

from .conduction import _thomas, _HAVE_SCIPY

if _HAVE_SCIPY:                                         # pragma: no cover
    from scipy.linalg import solve_banded


def step_implicit(T: np.ndarray, alpha: float, dx: float, dt: float) -> np.ndarray:
    """One backward-Euler step on a uniform slab with fixed (Dirichlet) ends."""
    n = T.size
    r = alpha * dt / dx**2
    ab = np.zeros((3, n))
    ab[0, 1:] = -r
    ab[1, :] = 1.0 + 2.0 * r
    ab[2, :-1] = -r
    ab[1, 0] = ab[1, -1] = 1.0            # ends held fixed
    ab[0, 1] = 0.0
    ab[2, -2] = 0.0
    if _HAVE_SCIPY:
        return solve_banded((1, 1), ab, T)
    return _thomas(ab, T)

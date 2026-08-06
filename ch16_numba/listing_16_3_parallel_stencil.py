"""Listing 16.3 -- A stencil smoother compiled and parallelized across cores
with prange (Jacobi update; independent rows, GIL-free).

Python for Engineers and Scientists, Chapter 16.
Run:  python listing_16_3_parallel_stencil.py
"""

from __future__ import annotations

import numpy as np
from numba import njit, prange


@njit(parallel=True, cache=True)
def gauss_seidel_sweep(T: np.ndarray, n_sweeps: int) -> np.ndarray:
    """Jacobi-style stencil sweeps, parallelized across rows with prange."""
    n = T.shape[0]
    for _ in range(n_sweeps):
        T_old = T.copy()
        for i in prange(1, n - 1):                 # parallel over rows
            for j in range(1, n - 1):
                T[i, j] = 0.25 * (T_old[i+1, j] + T_old[i-1, j] +
                                  T_old[i, j+1] + T_old[i, j-1])
    return T


if __name__ == "__main__":
    T = np.zeros((129, 129))
    T[-1, :] = 1.0                                 # hot top edge
    T = gauss_seidel_sweep(T, 2000)
    print(f"centre temperature = {T[64, 64]:.4f}   (expect ~0.25)")

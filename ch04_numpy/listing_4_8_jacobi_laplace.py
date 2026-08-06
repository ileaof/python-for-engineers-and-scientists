"""Listing 4.8 -- A complete Laplace solver: broadcasting boundaries, a stencil
update, and a reduction convergence test -- with no explicit loop over grid
points.

Python for Engineers and Scientists, Chapter 4.
Run:  python listing_4_8_jacobi_laplace.py
"""

import numpy as np


def jacobi_laplace(n=65, tol=1e-6, max_iter=20_000):
    """Solve Laplace's equation on a unit square with Dirichlet data.

    Top edge held at 1, other edges at 0. Returns the field and iteration count.
    """
    T = np.zeros((n, n))
    T[-1, :] = 1.0                                  # hot top edge (BC)

    for it in range(max_iter):
        T_new = T.copy()
        T_new[1:-1, 1:-1] = 0.25 * (                 # 5-point average
            T[2:, 1:-1] + T[:-2, 1:-1] +
            T[1:-1, 2:] + T[1:-1, :-2]
        )
        change = np.max(np.abs(T_new - T))           # L-inf residual (reduction)
        T = T_new
        if change < tol:
            return T, it
    return T, max_iter


if __name__ == "__main__":
    T, iters = jacobi_laplace()
    print(f"converged in {iters} iterations; T[32, 32] = {T[32, 32]:.4f}")

"""Listing 10.3 -- Successive over-relaxation (SOR) for Laplace's equation.
omega = 1 recovers Gauss-Seidel; 1 < omega < 2 accelerates convergence.

(Written as an explicit loop for clarity; vectorize or JIT it in production.)

Python for Engineers and Scientists, Chapter 10.
Run:  python listing_10_3_sor_laplace.py
"""

from __future__ import annotations

import numpy as np


def sor_laplace(n=65, omega=1.9, tol=1e-8, max_iter=20_000):
    """Solve Laplace's equation by successive over-relaxation (in place)."""
    T = np.zeros((n, n))
    T[-1, :] = 1.0                                    # hot top edge (BC)
    for it in range(max_iter):
        change = 0.0
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                gs = 0.25 * (T[i+1, j] + T[i-1, j] + T[i, j+1] + T[i, j-1])
                new = (1.0 - omega) * T[i, j] + omega * gs
                change = max(change, abs(new - T[i, j]))
                T[i, j] = new
        if change < tol:
            return T, it
    return T, max_iter


if __name__ == "__main__":
    T, iters = sor_laplace(n=41, omega=1.9)
    print(f"SOR converged in {iters} iterations; T[20, 20] = {T[20, 20]:.4f}")

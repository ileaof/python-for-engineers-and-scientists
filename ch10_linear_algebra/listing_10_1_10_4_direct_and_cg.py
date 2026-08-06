"""Listings 10.1 & 10.4 -- Dense direct solves with factorization reuse, and
conjugate gradient for a symmetric positive-definite sparse system.

Python for Engineers and Scientists, Chapter 10.
Run:  python listing_10_1_10_4_direct_and_cg.py
"""

from __future__ import annotations

import numpy as np
from scipy.linalg import solve, lu_factor, lu_solve
from scipy.sparse.linalg import cg

from listing_10_2_poisson_2d import poisson_2d

if __name__ == "__main__":
    # Listing 10.1 -- dense solve and factorization reuse
    A = np.array([[4.0, 1.0, 0.0],
                  [1.0, 4.0, 1.0],
                  [0.0, 1.0, 4.0]])
    b = np.array([1.0, 2.0, 3.0])
    x = solve(A, b)
    lu, piv = lu_factor(A)
    x1 = lu_solve((lu, piv), b)
    x2 = lu_solve((lu, piv), 2.0 * b)
    print("dense solve x      :", np.round(x, 5))
    print("reuse matches solve:", np.allclose(x1, x))

    # Listing 10.4 -- conjugate gradient on the sparse Poisson system
    n = 50
    Ap = poisson_2d(n)
    bp = np.ones(n * n)
    xp, info = cg(Ap, bp, rtol=1e-10, maxiter=2000)
    residual = np.linalg.norm(bp - Ap @ xp) / np.linalg.norm(bp)
    print(f"CG converged (info=={info}), rel. residual = {residual:.2e}")

"""Listing 5.1 -- A tridiagonal solve via scipy.linalg.solve_banded, O(n) in
time and memory, as used by the Graetz-problem solver.

Python for Engineers and Scientists, Chapter 5.
Run:  python listing_5_1_tridiagonal.py
"""

import numpy as np
from scipy.linalg import solve_banded


def solve_tridiagonal(a_sub, a_diag, a_super, rhs):
    """Solve a tridiagonal system A x = rhs using SciPy's banded solver.

    Parameters
    ----------
    a_sub, a_diag, a_super : ndarray
        Sub-, main, and super-diagonal of A (a_sub[0] and a_super[-1] unused).
    rhs : ndarray
        Right-hand side.

    Returns
    -------
    ndarray
        The solution x, in O(n) time and memory.
    """
    n = a_diag.size
    ab = np.zeros((3, n))          # banded storage: 3 rows for 3 diagonals
    ab[0, 1:] = a_super[:-1]       # super-diagonal (shifted right)
    ab[1, :] = a_diag              # main diagonal
    ab[2, :-1] = a_sub[1:]         # sub-diagonal (shifted left)
    return solve_banded((1, 1), ab, rhs)


if __name__ == "__main__":
    # A simple 1-D Poisson-like system: -u'' = 1, u(0)=u(1)=0
    n = 50
    a_diag = 2.0 * np.ones(n)
    a_sub = -1.0 * np.ones(n)
    a_super = -1.0 * np.ones(n)
    rhs = np.full(n, (1.0 / (n + 1)) ** 2)
    x = solve_tridiagonal(a_sub, a_diag, a_super, rhs)
    print("max displacement =", x.max())

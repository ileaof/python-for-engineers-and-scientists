"""Listing 10.2 -- Assembling and solving the sparse 2-D Poisson operator by
the Kronecker-sum construction (I (x) T + T (x) I).

Python for Engineers and Scientists, Chapter 10.
Run:  python listing_10_2_poisson_2d.py
"""

from __future__ import annotations

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve


def poisson_2d(n: int) -> sp.csr_matrix:
    """Sparse 2-D five-point Laplacian on an n x n interior grid."""
    main = 2.0 * np.ones(n)
    off = -1.0 * np.ones(n - 1)
    T = sp.diags([off, main, off], offsets=[-1, 0, 1])   # 1-D Laplacian
    I = sp.identity(n)
    return (sp.kron(I, T) + sp.kron(T, I)).tocsr()       # 2-D by Kron sum


if __name__ == "__main__":
    n = 50
    A = poisson_2d(n)
    b = np.ones(n * n)
    x = spsolve(A, b)
    density = A.nnz / (A.shape[0] * A.shape[1]) * 100
    print(f"N = {n*n}, nonzeros = {A.nnz}, density = {density:.3f} %")
    print(f"max solution value = {x.max():.5f}")

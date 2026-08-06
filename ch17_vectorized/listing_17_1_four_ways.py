"""Listing 17.1 -- One physical kernel (a Lennard-Jones energy sum) written four
ways: pure Python, NumPy vectorized, Numba, and (see Chapter 16) Numba parallel.
All fast versions agree to round-off.

Python for Engineers and Scientists, Chapter 17.
Run:  python listing_17_1_four_ways.py
"""

from __future__ import annotations

import numpy as np
from numba import njit


def lj_python(r):
    """Pure Python loop: clear, and slow."""
    total = 0.0
    for ri in r:
        total += 4.0 * (ri**-12 - ri**-6)
    return total


def lj_vectorized(r):
    """NumPy: one line, ~100x faster, but allocates temporaries."""
    return np.sum(4.0 * (r**-12 - r**-6))


@njit(cache=True)
def lj_numba(r):
    """Numba: compiled loop, fast AND allocation-free."""
    total = 0.0
    for i in range(r.size):
        ri = r[i]
        total += 4.0 * (ri**-12 - ri**-6)
    return total


if __name__ == "__main__":
    r = np.linspace(0.9, 3.0, 5_000_000)
    a, b, c = lj_python(r), lj_vectorized(r), lj_numba(r)   # warm up numba
    print(f"python     = {a:.4f}")
    print(f"vectorized = {b:.4f}")
    print(f"numba      = {c:.4f}")
    print("all agree:", np.allclose([a, b], c))

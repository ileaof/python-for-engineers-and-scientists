"""Listing 4.4 -- Views share memory; fancy indexing and .copy() do not.

Python for Engineers and Scientists, Chapter 4.
Run:  python listing_4_4_views_copies.py
"""

import numpy as np

a = np.arange(10.0)
inner = a[1:-1]          # a VIEW of elements 1..8, no copy
inner[:] = 0.0           # writes through: a is now [0, 0, ..., 0, 9]

b = a[1:-1].copy()       # an explicit COPY, independent of a
b[:] = -1.0              # leaves a untouched

mask = a > 5.0           # boolean mask, shape (10,)
big = a[mask]            # FANCY indexing -> always a copy
idx = np.array([0, 2, 4])
picked = a[idx]          # integer fancy indexing -> also a copy


if __name__ == "__main__":
    print("a      =", a)
    print("big    =", big)
    print("picked =", picked)
    print("view shares memory:", np.shares_memory(a, a[1:-1]))
    print("copy shares memory:", np.shares_memory(a, a[1:-1].copy()))

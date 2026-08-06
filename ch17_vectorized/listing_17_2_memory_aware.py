"""Listing 17.2 -- Reducing temporaries with in-place operations and the out=
argument of ufuncs. Both forms compute the identical result.

Python for Engineers and Scientists, Chapter 17.
Run:  python listing_17_2_memory_aware.py
"""

from __future__ import annotations

import numpy as np

if __name__ == "__main__":
    n = 10_000_000
    a = np.random.default_rng(0).random(n)

    # Allocates a temporary for each operation (several extra arrays):
    b_naive = np.sqrt(a**2 + 1.0) * 2.0

    # In-place / out= : reuse buffers, minimal new allocation:
    b = np.empty_like(a)
    np.square(a, out=b)          # b = a**2, no temporary
    b += 1.0                     # in place
    np.sqrt(b, out=b)            # in place
    b *= 2.0                     # in place

    print("results agree:", np.allclose(b_naive, b))

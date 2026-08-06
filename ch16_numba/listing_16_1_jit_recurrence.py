"""Listing 16.1 -- A sequential recurrence (the logistic map) compiled to
machine code with @njit; vectorization cannot help a step-depends-on-step loop.

Python for Engineers and Scientists, Chapter 16.
Run:  python listing_16_1_jit_recurrence.py
"""

from __future__ import annotations

import numpy as np
from numba import njit


@njit(cache=True)
def cumulative_logistic(x0: float, r: float, n: int) -> np.ndarray:
    """Iterate the logistic map x_{k+1} = r x_k (1 - x_k), n steps."""
    out = np.empty(n)
    x = x0
    for k in range(n):
        x = r * x * (1.0 - x)
        out[k] = x
    return out


if __name__ == "__main__":
    traj = cumulative_logistic(0.5, 3.9, 1_000_000)   # compiles on first call
    print(f"generated {traj.size} iterates; last = {traj[-1]:.6f}")

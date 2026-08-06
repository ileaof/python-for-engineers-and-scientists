"""Listing 11.3 -- 1-D transient conduction by the explicit (FTCS) scheme, with
a stability-limited time step (r = alpha dt / dx^2 <= 1/2).

Python for Engineers and Scientists, Chapter 11.
Run:  python listing_11_3_heat_explicit.py
"""

from __future__ import annotations

import numpy as np


def heat_explicit(n=101, alpha=1.0, L=1.0, t_end=0.05, safety=0.4):
    """1-D transient conduction by the explicit (FTCS) scheme.

    The time step is chosen from the stability limit dt <= dx^2 / (2 alpha).
    Initial condition: a hot centre; ends held at zero.
    """
    dx = L / (n - 1)
    dt = safety * dx**2 / alpha          # safety < 0.5 for stability
    x = np.linspace(0.0, L, n)
    T = np.exp(-200.0 * (x - 0.5) ** 2)  # a Gaussian hot spot
    T[0] = T[-1] = 0.0                    # Dirichlet ends

    r = alpha * dt / dx**2               # diffusion number (must be <= 0.5)
    steps = int(t_end / dt)
    for _ in range(steps):
        T[1:-1] += r * (T[2:] - 2.0 * T[1:-1] + T[:-2])   # stencil update
    return x, T, r


if __name__ == "__main__":
    x, T, r = heat_explicit()
    print(f"diffusion number r = {r:.3f}  (stable iff r <= 0.5)")
    print(f"peak temperature   = {T.max():.4f}")

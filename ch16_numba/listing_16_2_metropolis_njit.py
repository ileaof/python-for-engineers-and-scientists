"""Listing 16.2 -- The Metropolis inner loop compiled with @njit; verified
against the exact variance <x^2> = 1/(2 beta). Mirrors the Statistical
Thermodynamics package's metropolis_1d, with the potential inlined.

Python for Engineers and Scientists, Chapter 16.
Run:  python listing_16_2_metropolis_njit.py
"""

from __future__ import annotations

import numpy as np
from numba import njit


@njit(cache=True)
def metropolis_quadratic(beta: float, step: float, n_steps: int,
                         burn: int, seed: int) -> tuple:
    """Metropolis sampling of p(x) ~ exp(-beta x^2), a compiled hot loop."""
    np.random.seed(seed)                       # Numba-supported RNG
    x = 0.0
    Vx = x * x
    traj = np.empty(n_steps)
    n_acc = 0
    for i in range(n_steps + burn):
        xt = x + np.random.uniform(-step, step)
        Vt = xt * xt
        if Vt < Vx or np.random.random() < np.exp(-beta * (Vt - Vx)):
            x, Vx = xt, Vt
            if i >= burn:
                n_acc += 1
        if i >= burn:
            traj[i - burn] = x
    return traj, n_acc / n_steps


if __name__ == "__main__":
    traj, acc = metropolis_quadratic(beta=1.0, step=2.0, n_steps=1_000_000,
                                     burn=5000, seed=42)
    print(f"acceptance      = {acc:.3f}")
    print(f"<x^2> sampled   = {np.mean(traj**2):.4f}   (exact 0.5000)")

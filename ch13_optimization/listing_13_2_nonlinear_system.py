"""Listing 13.2 -- A nonlinear system for a two-junction pipe network, solved
with scipy.optimize.root.

Python for Engineers and Scientists, Chapter 13.
Run:  python listing_13_2_nonlinear_system.py
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import root


def two_junction_residual(heads, supply=(100.0, 60.0), k=(0.02, 0.03, 0.025)):
    """Continuity residuals at two junctions; zero at the solution."""
    H1, H2 = heads

    def q(dh, kk):
        return np.sign(dh) * np.sqrt(abs(dh) / kk)

    r1 = q(supply[0] - H1, k[0]) - q(H1 - H2, k[1])          # into junction 1
    r2 = q(H1 - H2, k[1]) - q(H2 - supply[1], k[2])          # into junction 2
    return [r1, r2]


if __name__ == "__main__":
    sol = root(two_junction_residual, x0=[90.0, 75.0], method="hybr")
    print("converged:", sol.success)
    print(f"junction heads = {sol.x[0]:.3f} m, {sol.x[1]:.3f} m")
    print(f"max residual   = {max(abs(r) for r in two_junction_residual(sol.x)):.1e}")

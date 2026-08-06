"""Chapter 23 (Listings 23.2-23.3) -- A unified steady-conduction finite-volume
solver for planar (m=0), cylindrical (m=1), and spherical (m=2) geometry,
verified against exact analytical profiles.

Adapted from the Heat Transfer case study. Requires scipy.
Run:  python conduction.py

Python for Engineers and Scientists, Chapter 23.
"""

from __future__ import annotations

import numpy as np
from scipy.linalg import solve_banded


def solve_conduction(r_faces, k, m, T_left, T_right, source=0.0):
    """Steady conduction on a 1-D radial mesh; m selects the geometry."""
    r_c = 0.5 * (r_faces[:-1] + r_faces[1:])
    n = r_c.size
    Af = r_faces ** m
    dr = np.diff(r_c)

    aW = np.zeros(n)
    aE = np.zeros(n)
    aW[1:] = k * Af[1:-1] / dr
    aE[:-1] = k * Af[1:-1] / dr
    aP = aW + aE
    b = source * (r_faces[1:] ** (m + 1) - r_faces[:-1] ** (m + 1)) / (m + 1)

    gl = k * Af[0] / (r_c[0] - r_faces[0])
    gr = k * Af[-1] / (r_faces[-1] - r_c[-1])
    aP[0] += gl
    b[0] += gl * T_left
    aP[-1] += gr
    b[-1] += gr * T_right

    ab = np.zeros((3, n))
    ab[0, 1:] = -aE[:-1]
    ab[1, :] = aP
    ab[2, :-1] = -aW[1:]
    return r_c, solve_banded((1, 1), ab, b)


def exact_conduction(r, m, r0, r1, T0, T1):
    """Exact source-free profile for each geometry."""
    if m == 0:
        return T0 + (T1 - T0) * (r - r0) / (r1 - r0)
    if m == 1:
        return T0 + (T1 - T0) * np.log(r / r0) / np.log(r1 / r0)
    if m == 2:
        return T0 + (T1 - T0) * (1 / r0 - 1 / r) / (1 / r0 - 1 / r1)
    raise ValueError("m must be 0, 1, or 2")


if __name__ == "__main__":
    names = {0: "planar", 1: "cylindrical", 2: "spherical"}
    for m in (0, 1, 2):
        r_faces = np.linspace(1.0, 2.0, 41)
        r_c, T = solve_conduction(r_faces, k=1.0, m=m, T_left=100.0, T_right=0.0)
        T_exact = exact_conduction(r_c, m, 1.0, 2.0, 100.0, 0.0)
        err = np.max(np.abs(T - T_exact))
        print(f"{names[m]:12s} (m={m}): max error vs exact = {err:.2e}")

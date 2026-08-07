"""Exact steady-conduction profiles for verification (Chapter 23)."""

from __future__ import annotations

import numpy as np


def exact_conduction(r, m, r0, r1, T0, T1):
    """Exact source-free profile: planar (linear), cylindrical (log), spherical (1/r)."""
    if m == 0:
        return T0 + (T1 - T0) * (r - r0) / (r1 - r0)
    if m == 1:
        return T0 + (T1 - T0) * np.log(r / r0) / np.log(r1 / r0)
    if m == 2:
        return T0 + (T1 - T0) * (1 / r0 - 1 / r) / (1 / r0 - 1 / r1)
    raise ValueError("m must be 0, 1, or 2")

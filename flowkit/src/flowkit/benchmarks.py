"""Benchmark data of Ghia, Ghia & Shin (1982) and comparison helpers."""

from __future__ import annotations

import numpy as np

# Vertical-centreline u-velocity, Re = 100.
GHIA_Y = np.array([0.0, 0.0547, 0.0625, 0.0703, 0.1016, 0.1719, 0.2813,
                   0.4531, 0.5, 0.6172, 0.7344, 0.8516, 0.9531, 0.9609,
                   0.9688, 0.9766, 1.0])
GHIA_U_RE100 = np.array([0.0, -0.03717, -0.04192, -0.04775, -0.06434,
                         -0.10150, -0.15662, -0.21090, -0.20581, -0.13641,
                         0.00332, 0.23151, 0.68717, 0.73722, 0.78871,
                         0.84123, 1.0])


def cavity_centreline_error(result: dict) -> float:
    """Max error of the computed vertical-centreline u vs the Ghia benchmark."""
    n = result["u"].shape[0] - 1
    y = np.linspace(0.0, 1.0, n + 1)
    u_centre = result["u"][n // 2, :]
    return float(np.max(np.abs(np.interp(GHIA_Y, y, u_centre) - GHIA_U_RE100)))

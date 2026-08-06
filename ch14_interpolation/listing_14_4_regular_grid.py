"""Listing 14.4 -- Interpolating a 2-D property table on a regular grid with
RegularGridInterpolator.

Python for Engineers and Scientists, Chapter 14.
Run:  python listing_14_4_regular_grid.py
"""

from __future__ import annotations

import numpy as np
from scipy.interpolate import RegularGridInterpolator

T = np.linspace(300.0, 500.0, 5)
p = np.linspace(1.0e5, 5.0e5, 4)
H = 1000.0 * T[:, None] + 1e-3 * p[None, :]         # h(T, p) on the grid

interp = RegularGridInterpolator((T, p), H, method="linear", bounds_error=True)


if __name__ == "__main__":
    query = np.array([[375.0, 2.5e5]])              # T = 375 K, p = 2.5 bar
    print(f"h(375 K, 2.5 bar) = {interp(query)[0]:.2f} J/kg")

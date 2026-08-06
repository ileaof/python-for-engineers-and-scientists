"""Listing 14.1 -- Piecewise-linear interpolation of a property table, with
extrapolation guarded (bounds_error=True).

Python for Engineers and Scientists, Chapter 14.
Run:  python listing_14_1_linear_table.py
"""

from __future__ import annotations

import numpy as np
from scipy.interpolate import interp1d

# A small property table: viscosity of water vs. temperature (Pa s)
T_table = np.array([280.0, 300.0, 320.0, 340.0, 360.0])
mu_table = np.array([1.43e-3, 8.90e-4, 5.77e-4, 4.20e-4, 3.24e-4])

mu = interp1d(T_table, mu_table, kind="linear", bounds_error=True)


if __name__ == "__main__":
    print(f"mu(310 K) linear = {float(mu(310.0)):.3e} Pa s")
    print(f"mu(310 K) np     = {np.interp(310.0, T_table, mu_table):.3e} Pa s")

"""Listing 5.4 -- A cubic spline to compare a solution against benchmark data
given on a different grid (e.g. Ghia et al. for the lid-driven cavity).

Python for Engineers and Scientists, Chapter 5.
Run:  python listing_5_4_interpolation.py
"""

import numpy as np
from scipy.interpolate import CubicSpline

# Benchmark data given at specific stations (e.g. Ghia et al.)
y_bench = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
u_bench = np.array([0.0, -0.21, -0.06, 0.23, 1.0])

# A cubic spline through the benchmark points
spline = CubicSpline(y_bench, u_bench)

# Evaluate the computed solution's stations against the smooth benchmark
y_query = np.linspace(0.0, 1.0, 65)
u_ref = spline(y_query)          # benchmark interpolated onto our grid


if __name__ == "__main__":
    print("u_ref at y=0.5 :", float(spline(0.5)))
    print("u_ref shape    :", u_ref.shape)

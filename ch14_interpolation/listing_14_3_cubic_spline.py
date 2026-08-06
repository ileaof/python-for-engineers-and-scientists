"""Listing 14.3 -- A cubic spline: smooth reconstruction, plus derivatives and
integrals for free.

Python for Engineers and Scientists, Chapter 14.
Run:  python listing_14_3_cubic_spline.py
"""

from __future__ import annotations

import numpy as np
from scipy.interpolate import CubicSpline

x = np.linspace(0.0, 2.0 * np.pi, 9)
y = np.sin(x)

spline = CubicSpline(x, y)
xf = np.linspace(0.0, 2.0 * np.pi, 400)


if __name__ == "__main__":
    err = np.max(np.abs(spline(xf) - np.sin(xf)))
    integral = spline.integrate(0.0, np.pi)
    print(f"cubic spline max error = {err:.3e}")
    print(f"spline integral 0..pi  = {integral:.6f}  (true 2.0)")

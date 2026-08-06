"""Listing 14.2 -- The Runge phenomenon: the error of a high-degree polynomial
through equally spaced nodes GROWS with degree.

Python for Engineers and Scientists, Chapter 14.
Run:  python listing_14_2_runge.py
"""

from __future__ import annotations

import numpy as np


def runge(x):
    """Runge's function, the classic counterexample."""
    return 1.0 / (1.0 + 25.0 * x**2)


def polynomial_interp_error(degree):
    """Max error of a degree-n polynomial through equally spaced nodes."""
    nodes = np.linspace(-1.0, 1.0, degree + 1)
    coeffs = np.polyfit(nodes, runge(nodes), degree)     # global polynomial
    fine = np.linspace(-1.0, 1.0, 1001)
    return np.max(np.abs(np.polyval(coeffs, fine) - runge(fine)))


if __name__ == "__main__":
    for degree in (4, 8, 12, 16):
        print(f"degree {degree:2d}: max error = {polynomial_interp_error(degree):.3e}")

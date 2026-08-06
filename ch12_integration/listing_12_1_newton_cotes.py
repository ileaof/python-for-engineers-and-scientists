"""Listing 12.1 -- Trapezoid vs. Simpson on a Gaussian; watch the error fall at
second and fourth order respectively.

Python for Engineers and Scientists, Chapter 12.
Run:  python listing_12_1_newton_cotes.py
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import trapezoid, simpson


def gaussian_integral(n):
    """Integrate exp(-x^2) on [-5, 5] with n points; true value ~ sqrt(pi)."""
    x = np.linspace(-5.0, 5.0, n)
    y = np.exp(-x**2)
    return trapezoid(y, x), simpson(y, x)


if __name__ == "__main__":
    exact = np.sqrt(np.pi)
    for n in (11, 21, 41, 81):
        tr, si = gaussian_integral(n)
        print(f"n={n:3d}  trapz err={abs(tr-exact):.2e}  simpson err={abs(si-exact):.2e}")

"""Listing 12.2 -- Gauss-Legendre quadrature: near-exact for smooth integrands
with very few points.

Python for Engineers and Scientists, Chapter 12.
Run:  python listing_12_2_gauss_legendre.py
"""

from __future__ import annotations

import numpy as np


def gauss_legendre_integral(f, a, b, n=8):
    """Integrate f on [a, b] with an n-point Gauss-Legendre rule."""
    nodes, weights = np.polynomial.legendre.leggauss(n)   # on [-1, 1]
    xm, xr = 0.5 * (a + b), 0.5 * (b - a)                  # map to [a, b]
    x = xm + xr * nodes
    return xr * np.sum(weights * f(x))


if __name__ == "__main__":
    exact = np.sqrt(np.pi)
    for n in (4, 8, 16):
        val = gauss_legendre_integral(lambda x: np.exp(-x**2), -5.0, 5.0, n)
        print(f"Gauss n={n:2d}: value={val:.10f}  err={abs(val-exact):.2e}")

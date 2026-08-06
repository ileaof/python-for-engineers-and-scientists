"""Listing 4.2 -- A ufunc-based, array-aware, numerically stable physical
function (the Einstein heat capacity), adapted from the Statistical
Thermodynamics package.

Python for Engineers and Scientists, Chapter 4.
Run:  python listing_4_2_heat_capacity.py
"""

import numpy as np


def harmonic_heat_capacity(T, theta=1.0, k_B=1.0):
    """Einstein heat capacity C/k_B = x^2 e^x / (e^x - 1)^2, x = theta/T.

    Written with e^{-x} internally so that it is numerically stable in the
    low-temperature (x large) limit, where e^{x} would overflow.
    """
    x = theta / np.asarray(T, float)      # accept scalar or array
    emx = np.exp(-x)                       # ufunc over the whole array
    return k_B * x ** 2 * emx / (1.0 - emx) ** 2


if __name__ == "__main__":
    T = np.array([0.1, 0.5, 1.0, 2.0, 10.0])
    print("T   =", T)
    print("C/k =", harmonic_heat_capacity(T))

"""Listing 12.3 -- Adaptive quad with a raised subdivision limit for a steep
integrand (a virial-type integral over a Lennard-Jones Mayer function),
mirroring the equilibrium module of the Statistical Thermodynamics package.

Python for Engineers and Scientists, Chapter 12.
Run:  python listing_12_3_adaptive_quad.py
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import quad


def second_virial_like(T_star, r_lo=1e-4, r_hi=12.0):
    """A virial-type integral over a Lennard-Jones Mayer function."""
    def mayer(r):
        u = 4.0 * (r**-12 - r**-6)               # LJ reduced potential
        return (np.exp(-u / T_star) - 1.0) * r**2

    value, abserr = quad(mayer, r_lo, r_hi, limit=400)
    return -2.0 * np.pi * value, abserr


if __name__ == "__main__":
    B2, err = second_virial_like(T_star=1.5)
    print(f"B2*(T*=1.5) = {B2:.6f}   (est. integration error {err:.1e})")

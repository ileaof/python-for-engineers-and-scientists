"""Listing 5.5 -- Special functions: the complementary error function (exact
transient-conduction benchmark) and the Riemann zeta function (Bose gas),
straight from scipy.special.

Python for Engineers and Scientists, Chapter 5.
Run:  python listing_5_5_special_functions.py
"""

import numpy as np
from scipy.special import erfc, zeta


def semi_infinite_temperature(x, t, alpha):
    """Dimensionless temperature in a semi-infinite solid, analytical.

    theta = (T - T_s) / (T_i - T_s) = erfc(x / (2 sqrt(alpha t))).
    """
    return erfc(x / (2.0 * np.sqrt(alpha * t)))     # vectorized special fn


if __name__ == "__main__":
    z_32 = zeta(1.5)     # ~2.612, appears in the condensation temperature
    z_52 = zeta(2.5)     # ~1.341, appears in the energy and pressure
    print(f"zeta(3/2) = {z_32:.4f}")
    print(f"zeta(5/2) = {z_52:.4f}")

    x = np.array([0.0, 0.01, 0.02, 0.05])
    theta = semi_infinite_temperature(x, t=100.0, alpha=1e-5)
    print("theta(x) =", theta)

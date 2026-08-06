"""Listing 1.4 -- Verification by two independent routes.

Compute the mean molecular speed both from the closed form and by numerically
integrating v f(v), and compare -- the book's central habit.

Python for Engineers and Scientists, Chapter 1.
Run:  python listing_1_4_verify_two_ways.py
"""

import numpy as np
from scipy.integrate import trapezoid

K_B = 1.380649e-23


def maxwell_pdf(v, m, T):
    """Maxwell-Boltzmann speed probability density f(v)."""
    a = m / (2.0 * K_B * T)
    return 4.0 * np.pi * (a / np.pi) ** 1.5 * v ** 2 * np.exp(-a * v ** 2)


def mean_speed_closed(m, T):
    return np.sqrt(8.0 * K_B * T / (np.pi * m))


def mean_speed_numerical(m, T, v_max=3000.0, n=200_001):
    """<v> = integral of v f(v) dv, by the composite trapezoidal rule."""
    v = np.linspace(0.0, v_max, n)
    return trapezoid(v * maxwell_pdf(v, m, T), v)


if __name__ == "__main__":
    m, T = 4.65e-26, 300.0
    exact = mean_speed_closed(m, T)
    numeric = mean_speed_numerical(m, T)
    rel_err = abs(numeric - exact) / exact
    print(f"closed form  <v> = {exact:10.4f} m/s")
    print(f"numerical    <v> = {numeric:10.4f} m/s")
    print(f"relative error   = {rel_err:.2e}")

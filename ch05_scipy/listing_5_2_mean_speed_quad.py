"""Listing 5.2 -- Adaptive quadrature to infinity with a self-reported error
estimate.

Python for Engineers and Scientists, Chapter 5.
Run:  python listing_5_2_mean_speed_quad.py
"""

import numpy as np
from scipy.integrate import quad

K_B = 1.380649e-23


def maxwell_pdf(v, m, T):
    a = m / (2.0 * K_B * T)
    return 4.0 * np.pi * (a / np.pi) ** 1.5 * v ** 2 * np.exp(-a * v ** 2)


def mean_speed_quad(m, T):
    """<v> by adaptive quadrature, with the estimated integration error."""
    integrand = lambda v: v * maxwell_pdf(v, m, T)
    value, abserr = quad(integrand, 0.0, np.inf)   # note: infinite upper limit
    return value, abserr


if __name__ == "__main__":
    m, T = 4.65e-26, 300.0
    v_mean, err = mean_speed_quad(m, T)
    exact = np.sqrt(8.0 * K_B * T / (np.pi * m))
    print(f"<v>   quad = {v_mean:.6f} m/s  (est. error {err:.1e})")
    print(f"<v> closed = {exact:.6f} m/s")

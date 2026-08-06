"""Listing 13.4 -- Nonlinear least-squares calibration of an Arrhenius rate law,
with parameter uncertainties from the covariance matrix.

Python for Engineers and Scientists, Chapter 13.
Run:  python listing_13_4_curve_fit.py
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import curve_fit


def arrhenius(T, A, Ea):
    """Reaction rate k(T) = A exp(-Ea / (R T)), R in J/(mol K)."""
    R = 8.314462618
    return A * np.exp(-Ea / (R * T))


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    T = np.linspace(300.0, 600.0, 12)
    true = arrhenius(T, A=1.0e9, Ea=6.0e4)
    data = true * (1.0 + 0.03 * rng.standard_normal(T.size))

    popt, pcov = curve_fit(arrhenius, T, data, p0=[1e8, 5e4])
    perr = np.sqrt(np.diag(pcov))
    print(f"A  = {popt[0]:.3e} +/- {perr[0]:.1e}   (true 1.0e9)")
    print(f"Ea = {popt[1]:.3e} +/- {perr[1]:.1e}   (true 6.0e4)")

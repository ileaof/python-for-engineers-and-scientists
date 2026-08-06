"""Listing 13.1 -- A combined radiative-convective surface-energy balance solved
robustly with brentq (Heat Transfer pattern).

Python for Engineers and Scientists, Chapter 13.
Run:  python listing_13_1_root_finding.py
"""

from __future__ import annotations

from scipy.optimize import brentq

SIGMA = 5.670374419e-8      # Stefan-Boltzmann constant, W/(m^2 K^4)


def surface_temperature(q_abs, eps, h, T_inf, T_lo=200.0, T_hi=2000.0):
    """Equilibrium surface T with both radiation and convection losses.

    Solves  eps*SIGMA*T^4 + h*(T - T_inf) = q_abs  by robust bracketing.
    """
    def balance(T):
        return eps * SIGMA * T**4 + h * (T - T_inf) - q_abs

    return brentq(balance, T_lo, T_hi, xtol=1e-12)


if __name__ == "__main__":
    T = surface_temperature(q_abs=1000.0, eps=0.9, h=15.0, T_inf=300.0)
    print(f"equilibrium surface temperature = {T:.4f} K")

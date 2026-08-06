"""Listing 5.3 -- A radiative-balance root found robustly with brentq,
following the surface-energy-balance pattern of the Heat Transfer examples.

Python for Engineers and Scientists, Chapter 5.
Run:  python listing_5_3_radiative_balance.py
"""

from scipy.optimize import brentq

SIGMA = 5.670374419e-8      # Stefan-Boltzmann constant, W/(m^2 K^4)


def equilibrium_temperature(q_abs, eps, T_lo=100.0, T_hi=2000.0):
    """Surface temperature at which emission balances an absorbed flux.

    Solves  eps * SIGMA * T^4 = q_abs  for T by robust bracketing.
    """
    def balance(T):
        return eps * SIGMA * T**4 - q_abs      # residual, zero at equilibrium

    return brentq(balance, T_lo, T_hi, xtol=1e-14)


if __name__ == "__main__":
    T_eq = equilibrium_temperature(q_abs=800.0, eps=0.9)
    print(f"equilibrium surface temperature = {T_eq:.4f} K")

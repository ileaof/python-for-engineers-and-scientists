"""Listings 11.1 & 11.2 -- Explicit Euler (verified against Newtonian cooling)
and the same problem with SciPy's adaptive solve_ivp.

Python for Engineers and Scientists, Chapter 11.
Run:  python listing_11_1_11_2_ode.py
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp


def euler(f, y0, t):
    """Explicit Euler for dy/dt = f(t, y) on the time grid t."""
    y = np.empty((t.size, np.size(y0)))
    y[0] = y0
    for n in range(t.size - 1):
        dt = t[n + 1] - t[n]
        y[n + 1] = y[n] + dt * f(t[n], y[n])
    return y


if __name__ == "__main__":
    k, T_inf, T0 = 0.7, 20.0, 90.0
    t = np.linspace(0.0, 5.0, 51)

    # Listing 11.1 -- explicit Euler vs exact
    T = euler(lambda _, T: -k * (T - T_inf), T0, t).ravel()
    exact = T_inf + (T0 - T_inf) * np.exp(-k * t)
    print(f"Euler   max error = {np.max(np.abs(T - exact)):.3e}")

    # Listing 11.2 -- adaptive RK45
    sol = solve_ivp(lambda t, T: -k * (T - T_inf), [0.0, 5.0], [T0],
                    method="RK45", rtol=1e-8, dense_output=True)
    T_rk = sol.sol(t)[0]
    print(f"RK45    max error = {np.max(np.abs(T_rk - exact)):.3e}")

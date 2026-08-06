"""Listing 13.3 -- One- and many-dimensional minimization: a Lennard-Jones well
(known minimum, so it verifies the optimizer) and the Rosenbrock valley.

Python for Engineers and Scientists, Chapter 13.
Run:  python listing_13_3_minimization.py
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import minimize_scalar, minimize


def lennard_jones(r, eps=1.0, sigma=1.0):
    return 4.0 * eps * ((sigma / r)**12 - (sigma / r)**6)


def rosenbrock(x):
    return sum(100.0 * (x[1:] - x[:-1]**2)**2 + (1.0 - x[:-1])**2)


if __name__ == "__main__":
    res1 = minimize_scalar(lennard_jones, bounds=(0.8, 3.0), method="bounded")
    res2 = minimize(rosenbrock, x0=np.zeros(4), method="BFGS")
    print(f"LJ minimum at r = {res1.x:.6f}  (analytic 2^(1/6) = {2**(1/6):.6f})")
    print(f"Rosenbrock min at x = {np.round(res2.x, 4)}  (true = all ones)")

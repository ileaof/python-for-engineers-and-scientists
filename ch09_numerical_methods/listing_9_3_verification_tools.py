"""Listing 9.3 -- Observed order, Richardson extrapolation and the Grid
Convergence Index (GCI): the verification core used by the case-study campaigns.

Python for Engineers and Scientists, Chapter 9.
Run:  python listing_9_3_verification_tools.py
"""

from __future__ import annotations

import numpy as np


def observed_order(f1: float, f2: float, f3: float, r: float = 2.0) -> float:
    """Observed order of accuracy from three grids refined by ratio r.

    f1 is the FINEST-grid result, f3 the coarsest. For a method of true
    order p, this returns ~p once the grids are fine enough to be asymptotic.
    """
    return np.log(abs((f3 - f2) / (f2 - f1))) / np.log(r)


def richardson(f1: float, f2: float, p: float, r: float = 2.0) -> float:
    """Richardson-extrapolated value from the two finest grids."""
    return f1 + (f1 - f2) / (r**p - 1.0)


def grid_convergence_index(f1: float, f2: float, p: float,
                           r: float = 2.0, fs: float = 1.25) -> float:
    """Roache's GCI (%) on the fine grid -- an error-bar for the solution."""
    return fs * abs((f1 - f2) / f1) / (r**p - 1.0) * 100.0


if __name__ == "__main__":
    # A second-order method: f(h) = f_exact + C h^2, f_exact = 1.0
    f_exact, Cc = 1.0, 0.5
    f1, f2, f3 = (f_exact + Cc * h**2 for h in (0.25, 0.5, 1.0))
    p = observed_order(f1, f2, f3)
    print(f"observed order p       = {p:.4f}")
    print(f"Richardson value       = {richardson(f1, f2, p):.8f}")
    print(f"GCI (fine grid)        = {grid_convergence_index(f1, f2, p):.4f} %")

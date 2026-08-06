"""Listing 12.4 -- A partition-function quantity computed by direct summation
over levels and by closed form -- the compute-two-ways verification applied to
integration/summation (from the Statistical Thermodynamics package).

Python for Engineers and Scientists, Chapter 12.
Run:  python listing_12_4_partition_sum.py
"""

from __future__ import annotations

import numpy as np


def harmonic_partition_sum(T, theta=1.0, n_max=400):
    """Harmonic partition function and energy by DIRECT summation over levels."""
    n = np.arange(n_max + 1)
    e = (n + 0.5) * theta                 # level energies (in units of theta)
    w = np.exp(-e / T)
    Z = w.sum()
    U = (e * w).sum() / Z                 # mean energy from the same weights
    return Z, U


def harmonic_energy_closed(T, theta=1.0):
    """Closed-form harmonic mean energy: 1/2 + 1/(e^{theta/T} - 1)."""
    x = theta / T
    return 0.5 + 1.0 / (np.exp(x) - 1.0)


if __name__ == "__main__":
    T = 1.3
    _, U_sum = harmonic_partition_sum(T)
    U_closed = harmonic_energy_closed(T)
    print(f"U (level sum)   = {U_sum:.10f}")
    print(f"U (closed form) = {U_closed:.10f}")
    print(f"agreement       = {abs(U_sum - U_closed):.1e}")

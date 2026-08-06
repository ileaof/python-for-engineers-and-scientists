"""Chapter 24 (Listings 24.2-24.3) -- Harmonic partition function two ways
(closed form vs direct level sum) and the blocking method for the error of a
correlated Monte Carlo series.

Adapted from the Statistical Thermodynamics package. NumPy only.
Run:  python partition_and_error.py

Python for Engineers and Scientists, Chapter 24.
"""

from __future__ import annotations

import numpy as np


def harmonic_energy(T, theta=1.0):
    """Closed-form mean energy: 1/2 + 1/(e^{theta/T} - 1)."""
    x = theta / np.asarray(T, float)
    return 0.5 + 1.0 / (np.exp(x) - 1.0)


def harmonic_partition_sum(T, theta=1.0, n_max=200):
    """Same physics by DIRECT summation over levels; returns (Z, U, E2)."""
    n = np.arange(n_max + 1)
    e = (n + 0.5) * theta
    w = np.exp(-e / T)
    Z = w.sum()
    U = (e * w).sum() / Z
    E2 = (e ** 2 * w).sum() / Z
    return float(Z), float(U), float(E2)


def blocking_error(series):
    """Standard error of a correlated series by the blocking method."""
    x = np.asarray(series, float)
    errors = []
    while x.size >= 4:
        errors.append(x.std(ddof=1) / np.sqrt(x.size))
        x = 0.5 * (x[0:-1:2] + x[1::2])
    return float(max(errors))


if __name__ == "__main__":
    T = 1.3
    _, U_sum, E2 = harmonic_partition_sum(T, n_max=400)
    U_closed = harmonic_energy(T)
    print(f"U closed vs sum: {U_closed:.10f} vs {U_sum:.10f}  "
          f"(diff {abs(U_closed - U_sum):.1e})")
    # Heat capacity from fluctuations should match the Einstein form.
    C_fluct = (E2 - U_sum**2) / T**2
    x = 1.0 / T
    C_einstein = x**2 * np.exp(x) / (np.exp(x) - 1.0)**2
    print(f"C fluctuation vs Einstein: {C_fluct:.6f} vs {C_einstein:.6f}")

    # Blocking error on a correlated AR(1) series vs the naive error.
    rng = np.random.default_rng(0)
    n, phi = 20000, 0.9
    s = np.empty(n)
    s[0] = rng.standard_normal()
    for i in range(1, n):
        s[i] = phi * s[i - 1] + rng.standard_normal()
    naive = s.std(ddof=1) / np.sqrt(n)
    print(f"blocking error {blocking_error(s):.4f} vs naive {naive:.4f} "
          f"(ratio {blocking_error(s)/naive:.1f})")

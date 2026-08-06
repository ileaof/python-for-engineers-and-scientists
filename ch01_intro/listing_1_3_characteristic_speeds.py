"""Listing 1.3 -- Characteristic speeds as reusable, documented software.

Python for Engineers and Scientists, Chapter 1.
Run:  python listing_1_3_characteristic_speeds.py
"""

from __future__ import annotations

import numpy as np

K_B: float = 1.380649e-23     # Boltzmann constant, J/K (CODATA/SI-2019, exact)


def characteristic_speeds(m: float, T: float) -> tuple[float, float, float]:
    """Most-probable, mean and root-mean-square speeds of a Maxwellian gas.

    Parameters
    ----------
    m : float
        Molecular mass in kilograms.
    T : float
        Temperature in kelvin.

    Returns
    -------
    tuple of float
        (v_p, v_mean, v_rms) in metres per second, satisfying
        v_p < v_mean < v_rms.
    """
    v_p = np.sqrt(2.0 * K_B * T / m)
    v_mean = np.sqrt(8.0 * K_B * T / (np.pi * m))
    v_rms = np.sqrt(3.0 * K_B * T / m)
    return float(v_p), float(v_mean), float(v_rms)


if __name__ == "__main__":
    m_N2 = 4.65e-26           # nitrogen molecule, kg
    vp, vm, vr = characteristic_speeds(m_N2, T=300.0)
    print(f"v_p    = {vp:7.1f} m/s")
    print(f"<v>    = {vm:7.1f} m/s")
    print(f"v_rms  = {vr:7.1f} m/s")

"""Listing 1.2 -- A correct but throwaway computation of characteristic speeds.

Python for Engineers and Scientists, Chapter 1.
Run:  python listing_1_2_speeds_throwaway.py
"""

import numpy as np

k_B = 1.380649e-23      # Boltzmann constant, J/K
m = 4.65e-26            # mass of an N2 molecule, kg
T = 300.0               # temperature, K

v_p = np.sqrt(2 * k_B * T / m)
v_mean = np.sqrt(8 * k_B * T / (np.pi * m))
v_rms = np.sqrt(3 * k_B * T / m)

print(v_p, v_mean, v_rms)

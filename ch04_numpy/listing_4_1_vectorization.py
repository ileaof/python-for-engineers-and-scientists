"""Listing 4.1 -- The same physics as an interpreted loop and as a vectorized
expression (local Reynolds number along a plate).

Python for Engineers and Scientists, Chapter 4.
Run:  python listing_4_1_vectorization.py
"""

import numpy as np

rho, mu = 1.184, 1.849e-5
U = 10.0
x = np.linspace(1e-4, 1.0, 1_000_000)     # positions along the plate

# (1) elementwise loop -- correct but slow, and verbose
Re = np.empty_like(x)
for idx in range(x.size):
    Re[idx] = rho * U * x[idx] / mu

# (2) vectorized -- one expression, ~100x faster, reads like the formula
Re = rho * U * x / mu


if __name__ == "__main__":
    print("Re[0]  =", Re[0])
    print("Re[-1] =", Re[-1])

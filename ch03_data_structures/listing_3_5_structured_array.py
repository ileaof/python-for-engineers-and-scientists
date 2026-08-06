"""Listing 3.5 -- A structured array as a typed, queryable property table.

Python for Engineers and Scientists, Chapter 3.
Run:  python listing_3_5_structured_array.py
"""

import numpy as np

species = np.array(
    [("N2", 28.0134, 3.36, 2.07),
     ("O2", 31.9988, 2.07, 2.26),
     ("CO", 28.0101, 2.78, 3.09)],
    dtype=[("name", "U4"),          # up to 4-character string
           ("M", "f8"),            # molar mass, g/mol
           ("theta_rot", "f8"),    # rotational temperature, K
           ("theta_vib", "f8")],   # vibrational temperature (x1000 K)
)


if __name__ == "__main__":
    print("names       =", species["name"])
    print("mean M      =", species["M"].mean())
    heavy = species[species["M"] > 28.0]
    print("M > 28 g/mol:", heavy["name"])

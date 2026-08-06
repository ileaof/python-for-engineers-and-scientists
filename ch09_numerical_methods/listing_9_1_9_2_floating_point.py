"""Listings 9.1 & 9.2 -- Machine epsilon, float comparison, and the condition
number as a predictor of digits lost in a linear solve.

Python for Engineers and Scientists, Chapter 9.
Run:  python listing_9_1_9_2_floating_point.py
"""

import numpy as np

if __name__ == "__main__":
    # Listing 9.1 -- machine epsilon and float comparison
    print("machine epsilon :", np.finfo(float).eps)
    print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)
    print("0.1 + 0.2 - 0.3 :", 0.1 + 0.2 - 0.3)
    print("np.isclose      :", np.isclose(0.1 + 0.2, 0.3))

    # Listing 9.2 -- conditioning
    A_good = np.array([[2.0, 1.0], [1.0, 3.0]])
    H = np.array([[1 / (i + j + 1) for j in range(6)] for i in range(6)])
    print(f"kappa(A_good)      = {np.linalg.cond(A_good):.1f}")
    print(f"kappa(Hilbert 6x6) = {np.linalg.cond(H):.2e}")

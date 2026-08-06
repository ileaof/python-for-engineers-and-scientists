"""Listing 3.3 -- Creating and inspecting arrays; shape and dtype.

Python for Engineers and Scientists, Chapter 3.
Run:  python listing_3_3_array_basics.py
"""

import numpy as np

T = np.zeros((64, 64), dtype=np.float64)   # a 64x64 temperature field
x = np.linspace(0.0, 1.0, 64)              # 64 points on [0, 1]
r = np.logspace(-3, 0, 50)                 # 50 points, log-spaced
J = np.arange(0, 2001)                     # 0, 1, ..., 2000 (rotor levels)


if __name__ == "__main__":
    print("T.shape =", T.shape)     # (64, 64)
    print("T.dtype =", T.dtype)     # float64
    print("T.size  =", T.size)      # 4096 elements
    print("T.ndim  =", T.ndim)      # 2 dimensions
    print("T.nbytes=", T.nbytes)    # 32768 bytes = 4096 * 8
    print("x[:3]   =", x[:3])
    print("r[:3]   =", r[:3])
    print("J[-1]   =", J[-1])

"""Listing 4.3 -- Broadcasting two axes into a 2-D field and evaluating a
function on it, with no loops and no materialized copies.

Python for Engineers and Scientists, Chapter 4.
Run:  python listing_4_3_broadcasting.py
"""

import numpy as np

x = np.linspace(0.0, 1.0, 5)       # shape (5,)
y = np.linspace(0.0, 2.0, 4)       # shape (4,)

# Reshape to a column and a row, then broadcast to a (4, 5) grid
X = x[np.newaxis, :]               # shape (1, 5)
Y = y[:, np.newaxis]              # shape (4, 1)

R = np.sqrt(X**2 + Y**2)           # shape (4, 5) -- no loops, no copies

# A Gaussian hot-spot evaluated on the whole grid at once
T = 300.0 + 50.0 * np.exp(-((X - 0.5)**2 + (Y - 1.0)**2) / 0.05)


if __name__ == "__main__":
    print("R.shape =", R.shape)
    print("T.shape =", T.shape)
    print("T max   =", T.max())

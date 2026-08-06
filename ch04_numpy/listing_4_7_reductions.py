"""Listing 4.7 -- Reductions and the axis argument, as used by solver
convergence monitors.

Python for Engineers and Scientists, Chapter 4.
Run:  python listing_4_7_reductions.py
"""

import numpy as np

resid = np.random.default_rng(0).random((64, 64))

l2 = np.sqrt(np.mean(resid**2))        # scalar RMS residual -> convergence test
linf = np.max(np.abs(resid))           # worst-cell residual
col_means = resid.mean(axis=0)         # shape (64,), one value per column
row_max = np.abs(resid).max(axis=1)    # shape (64,), one value per row


if __name__ == "__main__":
    print(f"L2 residual   = {l2:.4f}")
    print(f"Linf residual = {linf:.4f}")
    print("col_means shape =", col_means.shape)
    print("row_max shape   =", row_max.shape)

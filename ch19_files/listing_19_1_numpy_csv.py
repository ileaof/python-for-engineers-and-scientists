"""Listing 19.1 -- NumPy binary save/load (.npy, .npz) and a portable CSV export.

Python for Engineers and Scientists, Chapter 19.
Run:  python listing_19_1_numpy_csv.py
"""

from __future__ import annotations

import numpy as np

if __name__ == "__main__":
    x = np.linspace(0.0, 1.0, 101)
    T = np.exp(-((x - 0.5) / 0.1) ** 2)

    np.save("field.npy", T)
    T_back = np.load("field.npy")
    print("npy round trip exact:", np.array_equal(T, T_back))

    np.savez_compressed("solution.npz", x=x, T=T, alpha=1e-5)
    data = np.load("solution.npz")
    print("npz named access:", data["x"].shape, float(data["alpha"]))

    np.savetxt("profile.csv", np.column_stack([x, T]),
               delimiter=",", header="x,T", comments="")
    print("wrote profile.csv")

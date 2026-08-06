"""Listing 19.2 -- A self-describing HDF5 file: hierarchical datasets with
metadata attributes that travel WITH the data.

Requires: h5py, numpy.
Run:  python listing_19_2_hdf5.py

Python for Engineers and Scientists, Chapter 19.
"""

from __future__ import annotations

import h5py
import numpy as np


def save_solution(path, x, T, alpha, t_end):
    """Write a simulation result as a self-describing HDF5 file."""
    with h5py.File(path, "w") as f:
        f.create_dataset("grid/x", data=x, compression="gzip")
        f.create_dataset("fields/temperature", data=T, compression="gzip")
        f.attrs["title"] = "1-D transient conduction"
        f["fields/temperature"].attrs["units"] = "K"
        f["fields/temperature"].attrs["alpha_m2_s"] = alpha
        f["fields/temperature"].attrs["t_end_s"] = t_end


def load_solution(path):
    """Read the field and its metadata back."""
    with h5py.File(path, "r") as f:
        x = f["grid/x"][:]
        T = f["fields/temperature"][:]
        units = f["fields/temperature"].attrs["units"]
        alpha = f["fields/temperature"].attrs["alpha_m2_s"]
    return x, T, units, alpha


if __name__ == "__main__":
    x = np.linspace(0.0, 1.0, 101)
    T = np.exp(-((x - 0.5) / 0.1) ** 2)
    save_solution("run.h5", x, T, alpha=1e-5, t_end=0.05)
    x2, T2, units, alpha = load_solution("run.h5")
    print(f"loaded {T2.size} values in {units}, alpha={alpha:.1e}")

"""Listing 19.4 -- Exporting a 2-D structured flow field to Tecplot ASCII
(POINT) format -- the kind of post-processing export the Fluid Mechanics case
study produces.

Python for Engineers and Scientists, Chapter 19.
Run:  python listing_19_4_tecplot.py
"""

from __future__ import annotations

import numpy as np


def write_tecplot(path, x, y, u, v, p):
    """Write a 2-D structured field in Tecplot ASCII (point) format."""
    ny, nx = p.shape
    with open(path, "w") as f:
        f.write('TITLE = "Flow field"\n')
        f.write('VARIABLES = "x", "y", "u", "v", "p"\n')
        f.write(f'ZONE I={nx}, J={ny}, DATAPACKING=POINT\n')
        for j in range(ny):
            for i in range(nx):
                f.write(f"{x[i]:.6e} {y[j]:.6e} "
                        f"{u[j, i]:.6e} {v[j, i]:.6e} {p[j, i]:.6e}\n")


if __name__ == "__main__":
    x = np.linspace(0, 1, 16)
    y = np.linspace(0, 1, 16)
    U = np.zeros((16, 16))
    V = np.zeros((16, 16))
    P = np.zeros((16, 16))
    write_tecplot("cavity.dat", x, y, U, V, P)
    print("wrote cavity.dat")

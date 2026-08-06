"""Listings 4.5 & 4.6 -- The stencil idiom: second-order Laplacians expressed
as overlapping views, with no explicit loop over grid points.

Python for Engineers and Scientists, Chapter 4.
Run:  python listing_4_5_4_6_stencils.py
"""

import numpy as np


def laplacian_1d(u, dx):
    """Second derivative d2u/dx2 at interior points, second-order accurate."""
    lap = np.zeros_like(u)
    lap[1:-1] = (u[2:] - 2.0 * u[1:-1] + u[:-2]) / dx**2
    return lap


def laplacian_2d(u, dx, dy):
    """Five-point Laplacian on a 2-D grid, interior points only."""
    lap = np.zeros_like(u)
    lap[1:-1, 1:-1] = (
        (u[2:, 1:-1] - 2.0 * u[1:-1, 1:-1] + u[:-2, 1:-1]) / dx**2
        + (u[1:-1, 2:] - 2.0 * u[1:-1, 1:-1] + u[1:-1, :-2]) / dy**2
    )
    return lap


if __name__ == "__main__":
    # Verify against a known function: d2/dx2 sin(x) = -sin(x)
    x = np.linspace(0.0, np.pi, 201)
    dx = x[1] - x[0]
    u = np.sin(x)
    lap = laplacian_1d(u, dx)
    err = np.max(np.abs(lap[1:-1] - (-np.sin(x[1:-1]))))
    print(f"1-D Laplacian max error = {err:.2e}")

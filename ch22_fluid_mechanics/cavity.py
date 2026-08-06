"""Chapter 22 (Listings 22.2-22.4) -- A lid-driven-cavity solver by the
vorticity-streamfunction method, verified against Ghia, Ghia & Shin (1982).

Adapted from the Fluid Mechanics case study. NumPy only.
Run:  python cavity.py

Python for Engineers and Scientists, Chapter 22.
"""

from __future__ import annotations

import numpy as np


def solve_streamfunction(psi, omega, h, n_sweeps=15):
    """Advance Laplacian(psi) = -omega by n_sweeps Jacobi/SOR sweeps."""
    for _ in range(n_sweeps):
        psi[1:-1, 1:-1] = 0.25 * (
            psi[2:, 1:-1] + psi[:-2, 1:-1] +
            psi[1:-1, 2:] + psi[1:-1, :-2] +
            h * h * omega[1:-1, 1:-1]
        )
    return psi


def solve_cavity(n=64, reynolds=100.0, tol=1e-6, max_iter=40_000):
    """Solve the lid-driven cavity at a given Reynolds number."""
    h = 1.0 / n
    nu = 1.0 / reynolds
    psi = np.zeros((n + 1, n + 1))
    w = np.zeros((n + 1, n + 1))
    dt = 0.9 * min(h * h / (4 * nu), 0.5 * h)

    for it in range(max_iter):
        psi = solve_streamfunction(psi, w, h)
        u = np.zeros_like(psi)
        v = np.zeros_like(psi)
        u[1:-1, 1:-1] = (psi[1:-1, 2:] - psi[1:-1, :-2]) / (2 * h)
        v[1:-1, 1:-1] = -(psi[2:, 1:-1] - psi[:-2, 1:-1]) / (2 * h)
        u[:, -1] = 1.0                                   # moving lid

        w[:, -1] = -2 * psi[:, -2] / h**2 - 2 * 1.0 / h  # Thom's formula
        w[:, 0] = -2 * psi[:, 1] / h**2
        w[0, :] = -2 * psi[1, :] / h**2
        w[-1, :] = -2 * psi[-2, :] / h**2

        wxx = (w[2:, 1:-1] - 2 * w[1:-1, 1:-1] + w[:-2, 1:-1]) / h**2
        wyy = (w[1:-1, 2:] - 2 * w[1:-1, 1:-1] + w[1:-1, :-2]) / h**2
        wx = (w[2:, 1:-1] - w[:-2, 1:-1]) / (2 * h)
        wy = (w[1:-1, 2:] - w[1:-1, :-2]) / (2 * h)
        rhs = nu * (wxx + wyy) - u[1:-1, 1:-1] * wx - v[1:-1, 1:-1] * wy
        w_new = w[1:-1, 1:-1] + dt * rhs
        change = np.max(np.abs(w_new - w[1:-1, 1:-1]))
        w[1:-1, 1:-1] = w_new
        if change < tol and it > 100:
            return {"psi": psi, "omega": w, "u": u, "v": v, "iterations": it}
    return {"psi": psi, "omega": w, "u": u, "v": v, "iterations": max_iter}


# Ghia, Ghia & Shin (1982), Re = 100, vertical-centreline u.
GHIA_Y = np.array([0.0, 0.0547, 0.0625, 0.0703, 0.1016, 0.1719, 0.2813,
                   0.4531, 0.5, 0.6172, 0.7344, 0.8516, 0.9531, 0.9609,
                   0.9688, 0.9766, 1.0])
GHIA_U_RE100 = np.array([0.0, -0.03717, -0.04192, -0.04775, -0.06434,
                         -0.10150, -0.15662, -0.21090, -0.20581, -0.13641,
                         0.00332, 0.23151, 0.68717, 0.73722, 0.78871,
                         0.84123, 1.0])


def cavity_centreline_error(result):
    """Max error of the computed centreline u vs the Ghia benchmark."""
    n = result["u"].shape[0] - 1
    y = np.linspace(0.0, 1.0, n + 1)
    u_centre = result["u"][n // 2, :]
    return float(np.max(np.abs(np.interp(GHIA_Y, y, u_centre) - GHIA_U_RE100)))


if __name__ == "__main__":
    result = solve_cavity(n=64, reynolds=100.0, tol=1e-6)
    err = cavity_centreline_error(result)
    print(f"iterations = {result['iterations']}")
    print(f"max centreline error vs Ghia (Re=100, 64 grid) = {err:.4f}")

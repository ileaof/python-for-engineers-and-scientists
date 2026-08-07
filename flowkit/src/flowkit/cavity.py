"""Lid-driven cavity by the vorticity-streamfunction method (Chapter 22).

Adapted from the Fluid Mechanics case study; verified against Ghia et al. (1982).
"""

from __future__ import annotations

import numpy as np

from .poisson import solve_streamfunction


def solve_cavity(n: int = 64, reynolds: float = 100.0,
                 tol: float = 1e-6, max_iter: int = 40_000) -> dict:
    """Solve the lid-driven cavity at a given Reynolds number.

    Parameters
    ----------
    n : int
        Number of cells per side (grid is (n+1) x (n+1) nodes).
    reynolds : float
        Reynolds number based on lid speed and cavity width.
    tol : float
        Convergence tolerance on the max vorticity change.
    max_iter : int
        Iteration cap.

    Returns
    -------
    dict
        Keys: ``psi``, ``omega``, ``u``, ``v`` (fields) and ``iterations``.
    """
    h = 1.0 / n
    nu = 1.0 / reynolds
    psi = np.zeros((n + 1, n + 1))
    w = np.zeros((n + 1, n + 1))
    dt = 0.9 * min(h * h / (4 * nu), 0.5 * h)     # stable pseudo-time step

    for it in range(max_iter):
        psi = solve_streamfunction(psi, w, h)

        u = np.zeros_like(psi)
        v = np.zeros_like(psi)
        u[1:-1, 1:-1] = (psi[1:-1, 2:] - psi[1:-1, :-2]) / (2 * h)
        v[1:-1, 1:-1] = -(psi[2:, 1:-1] - psi[:-2, 1:-1]) / (2 * h)
        u[:, -1] = 1.0                             # moving lid (top)

        w[:, -1] = -2 * psi[:, -2] / h**2 - 2 * 1.0 / h    # Thom's formula (lid)
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

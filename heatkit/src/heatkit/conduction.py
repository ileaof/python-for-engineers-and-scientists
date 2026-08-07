"""Unified steady-conduction finite-volume solver (Chapter 23).

One assembly handles planar (m=0), cylindrical (m=1) and spherical (m=2)
geometry via face areas A ~ r**m, solved as a tridiagonal system.
"""

from __future__ import annotations

import numpy as np

try:
    from scipy.linalg import solve_banded
    _HAVE_SCIPY = True
except ImportError:                                    # pragma: no cover
    _HAVE_SCIPY = False


def _thomas(ab: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Tridiagonal solve (Thomas) using scipy banded storage, no SciPy needed."""
    n = b.size
    sup = ab[0].copy()
    diag = ab[1].copy()
    sub = ab[2].copy()
    d = b.copy()
    for i in range(1, n):
        w = sub[i - 1] / diag[i - 1]
        diag[i] -= w * sup[i]
        d[i] -= w * d[i - 1]
    x = np.zeros(n)
    x[-1] = d[-1] / diag[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - sup[i + 1] * x[i + 1]) / diag[i]
    return x


def solve_conduction(mesh, k: float, m: int, T_left: float, T_right: float,
                     source: float = 0.0) -> np.ndarray:
    """Steady conduction on a RadialMesh; m selects the geometry.

    Parameters
    ----------
    mesh : heatkit.mesh.RadialMesh
        The radial mesh.
    k : float
        Thermal conductivity.
    m : int
        Geometry: 0 planar, 1 cylindrical, 2 spherical.
    T_left, T_right : float
        Dirichlet wall temperatures at r0 and r1.
    source : float, optional
        Uniform volumetric source.

    Returns
    -------
    numpy.ndarray
        Cell-centre temperatures.
    """
    r_faces = mesh.faces
    r_c = mesh.centers
    n = r_c.size
    Af = r_faces ** m
    dr = np.diff(r_c)

    aW = np.zeros(n)
    aE = np.zeros(n)
    aW[1:] = k * Af[1:-1] / dr
    aE[:-1] = k * Af[1:-1] / dr
    aP = aW + aE
    b = source * (r_faces[1:] ** (m + 1) - r_faces[:-1] ** (m + 1)) / (m + 1)

    gl = k * Af[0] / (r_c[0] - r_faces[0])
    gr = k * Af[-1] / (r_faces[-1] - r_c[-1])
    aP[0] += gl
    b[0] += gl * T_left
    aP[-1] += gr
    b[-1] += gr * T_right

    ab = np.zeros((3, n))
    ab[0, 1:] = -aE[:-1]
    ab[1, :] = aP
    ab[2, :-1] = -aW[1:]

    if _HAVE_SCIPY:
        return solve_banded((1, 1), ab, b)
    return _thomas(ab, b)

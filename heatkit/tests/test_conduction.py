"""Tests for the unified conduction solver."""

import numpy as np

from heatkit.mesh import RadialMesh
from heatkit.conduction import solve_conduction
from heatkit.analytical import exact_conduction


def test_planar_reproduces_linear_to_roundoff():
    mesh = RadialMesh(1.0, 2.0, 40)
    T = solve_conduction(mesh, k=1.0, m=0, T_left=100.0, T_right=0.0)
    T_exact = exact_conduction(mesh.centers, 0, 1.0, 2.0, 100.0, 0.0)
    assert np.max(np.abs(T - T_exact)) < 1e-10       # exact for a linear field


def test_cylindrical_and_spherical_converge():
    for m in (1, 2):
        coarse = RadialMesh(1.0, 2.0, 20)
        fine = RadialMesh(1.0, 2.0, 80)
        ec = np.max(np.abs(solve_conduction(coarse, 1.0, m, 100.0, 0.0)
                           - exact_conduction(coarse.centers, m, 1.0, 2.0, 100.0, 0.0)))
        ef = np.max(np.abs(solve_conduction(fine, 1.0, m, 100.0, 0.0)
                           - exact_conduction(fine.centers, m, 1.0, 2.0, 100.0, 0.0)))
        assert ef < ec                                # error falls with refinement

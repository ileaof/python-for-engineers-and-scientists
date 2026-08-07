"""Tests for the lid-driven-cavity solver."""

import numpy as np

from flowkit.cavity import solve_cavity
from flowkit.benchmarks import cavity_centreline_error


def test_cavity_matches_ghia_re100():
    result = solve_cavity(n=64, reynolds=100.0, tol=1e-6)
    assert cavity_centreline_error(result) < 0.05     # within 5% on a 64 grid


def test_cavity_converges_with_refinement():
    e32 = cavity_centreline_error(solve_cavity(n=32, reynolds=100.0))
    e64 = cavity_centreline_error(solve_cavity(n=64, reynolds=100.0))
    assert e64 < e32

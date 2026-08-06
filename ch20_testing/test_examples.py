"""Chapter 20 (Listings 20.1-20.3) -- A runnable pytest suite illustrating the
book's testing patterns: known values with tolerance, exact scaling laws,
compute-two-ways checks, fixtures, and parametrization.

Requires: pytest, numpy.
Run:  pytest test_examples.py -v

Python for Engineers and Scientists, Chapter 20.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pytest


# --- code under test (would normally be imported from the library) ---------
def thermal_diffusivity(k, rho, cp):
    return k / (rho * cp)


# --- Listing 20.1: a known value (with tolerance) and an exact scaling law ---
def test_thermal_diffusivity_air():
    alpha = thermal_diffusivity(0.02551, 1.184, 1007.0)
    assert np.isclose(alpha, 2.14e-5, rtol=1e-2)


def test_diffusivity_scales_inversely_with_density():
    a1 = thermal_diffusivity(1.0, 1.0, 1.0)
    a2 = thermal_diffusivity(1.0, 2.0, 1.0)
    assert np.isclose(a2, a1 / 2.0)


# --- Listing 20.2 spirit: compute two ways and compare -----------------------
def test_partition_energy_two_ways():
    """Harmonic mean energy: level sum vs closed form (Chapter 12)."""
    T, theta = 1.3, 1.0
    n = np.arange(401)
    w = np.exp(-(n + 0.5) * theta / T)
    U_sum = np.sum((n + 0.5) * theta * w) / np.sum(w)
    U_closed = 0.5 + 1.0 / (np.exp(theta / T) - 1.0)
    assert np.isclose(U_sum, U_closed, rtol=1e-8)


# --- Listing 20.3: a fixture and parametrization -----------------------------
@pytest.fixture
def air():
    @dataclass(frozen=True)
    class Fluid:
        rho: float = 1.184
        mu: float = 1.849e-5
        k: float = 0.02551
        cp: float = 1007.0

    return Fluid()


def test_prandtl_is_order_one(air):
    Pr = air.mu * air.cp / air.k
    assert 0.6 < Pr < 0.8


@pytest.mark.parametrize("rho, cp, expected_sign", [
    (1.0, 1.0, 1.0),
    (2.0, 1.0, 1.0),
    (0.5, 2.0, 1.0),
])
def test_diffusivity_positive(rho, cp, expected_sign):
    assert np.sign(thermal_diffusivity(1.0, rho, cp)) == expected_sign

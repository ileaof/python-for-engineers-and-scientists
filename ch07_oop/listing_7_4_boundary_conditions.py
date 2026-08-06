"""Listing 7.4 -- An abstract base class with concrete boundary conditions,
demonstrating inheritance and polymorphism (as used by the conduction solvers).

Python for Engineers and Scientists, Chapter 7.
Run:  python listing_7_4_boundary_conditions.py
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import numpy as np


class BoundaryCondition(ABC):
    """Abstract boundary condition applied to the edge of a 1-D field."""

    @abstractmethod
    def apply(self, u: np.ndarray, dx: float) -> None:
        """Modify the ghost/edge value of u in place to enforce the BC."""


class Dirichlet(BoundaryCondition):
    """Fix the boundary value: u[0] = value."""

    def __init__(self, value: float) -> None:
        self.value = value

    def apply(self, u: np.ndarray, dx: float) -> None:
        u[0] = self.value


class Neumann(BoundaryCondition):
    """Fix the boundary gradient: (u[1] - u[0]) / dx = flux."""

    def __init__(self, flux: float) -> None:
        self.flux = flux

    def apply(self, u: np.ndarray, dx: float) -> None:
        u[0] = u[1] - self.flux * dx


def apply_left_bc(u: np.ndarray, dx: float, bc: BoundaryCondition) -> None:
    """Apply ANY boundary condition -- polymorphism in one line."""
    bc.apply(u, dx)


if __name__ == "__main__":
    u = np.linspace(1.0, 2.0, 6)
    apply_left_bc(u, dx=0.2, bc=Dirichlet(0.0))
    print("after Dirichlet(0):", u)
    apply_left_bc(u, dx=0.2, bc=Neumann(1.0))
    print("after Neumann(1):  ", u)

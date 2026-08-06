"""Listing 7.5 -- A Protocol defines an interface by structure, not inheritance.

Python for Engineers and Scientists, Chapter 7.
Run:  python listing_7_5_solver_protocol.py
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class Solver(Protocol):
    """Anything with this method counts as a Solver -- no inheritance needed."""

    def solve(self, tol: float) -> dict: ...


def run_and_report(solver: Solver, tol: float = 1e-6) -> None:
    """Accept ANY object that has a solve(tol) -> dict method."""
    result = solver.solve(tol)
    print(f"converged: {result}")


class DummySolver:
    """Satisfies the Solver protocol structurally, without inheriting it."""

    def solve(self, tol: float) -> dict:
        return {"iterations": 42, "residual": tol / 10.0}


if __name__ == "__main__":
    s = DummySolver()
    print("is a Solver:", isinstance(s, Solver))
    run_and_report(s)

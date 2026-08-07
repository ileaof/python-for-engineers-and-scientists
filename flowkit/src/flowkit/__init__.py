"""flowkit -- a small computational-fluid-dynamics package.

Companion to *Python for Engineers and Scientists* (Chapter 22). Solves the
lid-driven cavity by the vorticity-streamfunction method and verifies it against
the benchmark of Ghia, Ghia & Shin (1982).
"""

from __future__ import annotations

from . import benchmarks, cavity, mesh, poisson

__version__ = "1.0.0"
__author__ = "I. L. Ferreira"
__license__ = "MIT"

__all__ = ["mesh", "poisson", "cavity", "benchmarks", "__version__"]

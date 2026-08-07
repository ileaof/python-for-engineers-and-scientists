"""heatkit -- a unified conduction package.

Companion to *Python for Engineers and Scientists* (Chapter 23). A single
finite-volume solver handles planar (m=0), cylindrical (m=1) and spherical (m=2)
conduction, verified against exact analytical profiles, plus an implicit
transient solver.
"""

from __future__ import annotations

from . import analytical, conduction, mesh, transient

__version__ = "1.0.0"
__author__ = "I. L. Ferreira"
__license__ = "MIT"

__all__ = ["mesh", "conduction", "analytical", "transient", "__version__"]

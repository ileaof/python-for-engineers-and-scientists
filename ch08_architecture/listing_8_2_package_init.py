"""Listing 8.2 -- A curated public API: the package's front door.

This is the reference form of a package __init__.py. In a real project it lives
at src/<package_name>/__init__.py; the relative imports below assume sibling
modules (constants.py, partition_functions.py, ...). It is reproduced here as a
standalone reference, so the relative imports are shown but commented.

Python for Engineers and Scientists, Chapter 8.
"""

from __future__ import annotations

# In a real package these are relative imports of sibling modules:
#
# from . import (
#     constants,
#     partition_functions,
#     thermodynamics,
#     kinetic_theory,
#     quantum_statistics,
#     numerical_methods,
#     plotting,
# )

__version__ = "1.0.0"
__author__ = "I. L. Ferreira"
__license__ = "MIT"

__all__ = [
    "constants",
    "partition_functions",
    "thermodynamics",
    "kinetic_theory",
    "quantum_statistics",
    "numerical_methods",
    "plotting",
    "__version__",
]


if __name__ == "__main__":
    print(f"package version {__version__} by {__author__} ({__license__})")
    print("public API:", ", ".join(n for n in __all__ if not n.startswith("__")))

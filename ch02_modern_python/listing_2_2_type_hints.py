"""Listing 2.2 -- Type hints document intent for readers and tools alike.

Python for Engineers and Scientists, Chapter 2.
"""

from __future__ import annotations


def thermal_diffusivity(k: float, rho: float, cp: float) -> float:
    """Thermal diffusivity alpha = k / (rho * cp), in m^2/s."""
    return k / (rho * cp)


if __name__ == "__main__":
    # air at 300 K
    print(f"alpha = {thermal_diffusivity(0.02551, 1.184, 1007.0):.3e} m^2/s")

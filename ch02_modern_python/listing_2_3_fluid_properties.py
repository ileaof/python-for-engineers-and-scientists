"""Listing 2.3 -- A frozen dataclass modelling immutable fluid properties.

Derived quantities (kinematic viscosity, thermal diffusivity, Prandtl number)
are exposed as properties, computed on demand so they cannot fall out of sync.

Python for Engineers and Scientists, Chapter 2.
Run:  python listing_2_3_fluid_properties.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FluidProperties:
    """Constant thermophysical properties of a Newtonian fluid (SI units)."""

    rho: float          # density, kg/m^3
    mu: float           # dynamic viscosity, Pa s
    k: float            # thermal conductivity, W/(m K)
    cp: float           # specific heat, J/(kg K)

    @property
    def nu(self) -> float:
        """Kinematic viscosity nu = mu / rho, in m^2/s."""
        return self.mu / self.rho

    @property
    def alpha(self) -> float:
        """Thermal diffusivity alpha = k / (rho * cp), in m^2/s."""
        return self.k / (self.rho * self.cp)

    @property
    def Pr(self) -> float:
        """Prandtl number Pr = nu / alpha = mu * cp / k (dimensionless)."""
        return self.nu / self.alpha


if __name__ == "__main__":
    air = FluidProperties(rho=1.184, mu=1.849e-5, k=0.02551, cp=1007.0)
    print(f"nu    = {air.nu:.3e} m^2/s")
    print(f"alpha = {air.alpha:.3e} m^2/s")
    print(f"Pr    = {air.Pr:.4f}")

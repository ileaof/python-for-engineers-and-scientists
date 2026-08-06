"""Listings 7.2 & 7.3 -- A hydraulic reservoir network by object-oriented
design: an immutable Pipe that owns its own physics, composed into a
ReservoirNetwork that enforces junction continuity.

Adapted from the Fluid Mechanics case study (three-reservoir problem).

Python for Engineers and Scientists, Chapter 7.
Run:  python listing_7_2_7_3_reservoir_network.py
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.optimize import brentq

G = 9.81          # gravitational acceleration, m/s^2
NU = 1.0e-6       # kinematic viscosity of water, m^2/s


def colebrook(Re: float, eps_D: float) -> float:
    """Darcy friction factor: laminar below Re=2300, else Colebrook."""
    if Re < 2300.0:
        return 64.0 / max(Re, 1e-6)
    return brentq(
        lambda f: 1.0 / np.sqrt(f)
        + 2.0 * np.log10(eps_D / 3.7 + 2.51 / (Re * np.sqrt(f))),
        1e-4, 1.0, xtol=1e-12,
    )


@dataclass(frozen=True, slots=True)
class Pipe:
    """A pipe from a reservoir (surface elevation z) to a common junction."""

    z: float                 # reservoir surface elevation, m
    L: float                 # length, m
    D: float                 # diameter, m
    eps: float = 4.5e-5      # wall roughness, m
    Kminor: float = 0.5      # minor-loss coefficient

    @property
    def area(self) -> float:
        """Cross-sectional area, m^2."""
        return np.pi * self.D**2 / 4.0

    def flow_to_junction(self, H_junction: float) -> float:
        """Signed volumetric flow from this reservoir toward H_junction.

        Positive means flow INTO the junction. Solves the head-loss balance
        by fixed-point iteration on the friction factor (which depends on Re).
        """
        dz = self.z - H_junction
        if abs(dz) < 1e-14:
            return 0.0
        Q = np.sign(dz) * 1e-3
        for _ in range(100):
            V = abs(Q) / self.area
            Re = V * self.D / NU
            f = colebrook(Re, self.eps / self.D)
            coeff = (f * self.L / self.D + self.Kminor) / (2 * G * self.area**2)
            Q_new = np.sign(dz) * np.sqrt(abs(dz) / coeff)
            if abs(Q_new - Q) < 1e-12:
                return Q_new
            Q = Q_new
        return Q


@dataclass
class ReservoirNetwork:
    """Several reservoirs feeding one junction; find the balancing head."""

    pipes: list[Pipe]

    def net_flow(self, H_junction: float) -> float:
        """Sum of signed flows into the junction; zero at the solution."""
        return sum(p.flow_to_junction(H_junction) for p in self.pipes)

    def solve_junction_head(self) -> float:
        """Junction head H_J at which continuity closes, by bracketing."""
        z_lo = min(p.z for p in self.pipes) + 1e-6
        z_hi = max(p.z for p in self.pipes) - 1e-6
        return brentq(self.net_flow, z_lo, z_hi, xtol=1e-10)


if __name__ == "__main__":
    network = ReservoirNetwork([
        Pipe(z=100.0, L=1000.0, D=0.30),
        Pipe(z=80.0, L=1200.0, D=0.25),
        Pipe(z=60.0, L=800.0, D=0.20),
    ])
    H_J = network.solve_junction_head()
    flows = [p.flow_to_junction(H_J) for p in network.pipes]
    print(f"junction head H_J = {H_J:.4f} m")
    for k, (p, Q) in enumerate(zip(network.pipes, flows), 1):
        print(f"  pipe {k}: z={p.z:5.0f} m  Q={Q * 1e3:+7.2f} L/s")
    print(f"continuity residual = {sum(flows):.2e} m^3/s")

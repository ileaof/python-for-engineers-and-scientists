"""Listing 2.4 -- A configuration dataclass with defaults, a mutable-default
guard (field(default_factory=...)), and validation in __post_init__.

Python for Engineers and Scientists, Chapter 2.
Run:  python listing_2_4_simulation_config.py
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SimulationConfig:
    """Parameters controlling a finite-volume run."""

    nx: int = 64                      # cells in x
    ny: int = 64                      # cells in y
    reynolds: float = 100.0           # Reynolds number
    tol: float = 1.0e-6               # convergence tolerance
    max_iter: int = 40_000            # iteration cap
    relax: float = 0.7                # under-relaxation factor
    monitors: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.nx < 2 or self.ny < 2:
            raise ValueError("grid must be at least 2x2")
        if not 0.0 < self.relax <= 1.0:
            raise ValueError("relax must lie in (0, 1]")


if __name__ == "__main__":
    cfg = SimulationConfig(nx=128, ny=128, reynolds=400.0)
    print(cfg)

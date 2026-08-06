"""Listing 15.1 -- An embarrassingly parallel parameter sweep with a process
pool. Note the REQUIRED if __name__ == "__main__" guard for multiprocessing.

Python for Engineers and Scientists, Chapter 15.
Run:  python listing_15_1_parameter_sweep.py
"""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor

import numpy as np


def run_case(reynolds: float) -> tuple[float, float]:
    """A stand-in for one expensive solver run; returns (Re, a result)."""
    rng = np.random.default_rng(int(reynolds))
    result = np.mean(rng.random(2_000_000))          # CPU-bound busywork
    return reynolds, result


def sweep(reynolds_values: list[float], workers: int = 4) -> dict:
    """Run run_case for every Reynolds number, in parallel across processes."""
    with ProcessPoolExecutor(max_workers=workers) as pool:
        results = pool.map(run_case, reynolds_values)
    return dict(results)


if __name__ == "__main__":                # REQUIRED guard for multiprocessing
    Re = [100.0, 200.0, 400.0, 800.0, 1000.0, 1600.0]
    out = sweep(Re, workers=4)
    for r, val in out.items():
        print(f"Re={r:7.1f}  result={val:.6f}")

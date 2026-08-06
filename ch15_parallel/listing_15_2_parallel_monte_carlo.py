"""Listing 15.2 -- Independent Monte Carlo chains in parallel, with correctly
spawned (independent, reproducible) RNG streams via SeedSequence.spawn.

Python for Engineers and Scientists, Chapter 15.
Run:  python listing_15_2_parallel_monte_carlo.py
"""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor

import numpy as np


def mc_mean(seed: int, n: int = 2_000_000) -> float:
    """One independent Monte Carlo estimate of E[x^2], x ~ U(0,1); true 1/3."""
    rng = np.random.default_rng(seed)                # independent stream
    return float(np.mean(rng.random(n) ** 2))


def parallel_monte_carlo(n_chains: int = 8, workers: int = 4) -> tuple:
    """Run independent chains in parallel; combine into a mean and its error."""
    root = np.random.SeedSequence(12345)
    seeds = [int(s.generate_state(1)[0]) for s in root.spawn(n_chains)]
    with ProcessPoolExecutor(max_workers=workers) as pool:
        estimates = list(pool.map(mc_mean, seeds))
    estimates = np.array(estimates)
    mean = estimates.mean()
    stderr = estimates.std(ddof=1) / np.sqrt(n_chains)   # error of the mean
    return mean, stderr


if __name__ == "__main__":
    mean, stderr = parallel_monte_carlo()
    print(f"E[x^2] = {mean:.6f} +/- {stderr:.6f}   (true 0.333333)")

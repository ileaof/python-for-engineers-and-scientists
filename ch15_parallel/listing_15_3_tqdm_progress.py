"""Listing 15.3 -- A parallel sweep with a live tqdm progress bar via
as_completed (updates as each task finishes).

Python for Engineers and Scientists, Chapter 15.
Run:  python listing_15_3_tqdm_progress.py
"""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor, as_completed

import numpy as np
from tqdm import tqdm


def _worker(x: float) -> float:
    rng = np.random.default_rng(int(x * 1000))
    return float(np.mean(rng.random(500_000)))


def sweep_with_progress(values, worker, max_workers=4):
    """Parallel map that shows a live progress bar as tasks finish."""
    results = {}
    with ProcessPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(worker, v): v for v in values}
        for fut in tqdm(as_completed(futures), total=len(futures),
                        desc="parameter sweep"):
            v = futures[fut]
            results[v] = fut.result()
    return results


if __name__ == "__main__":
    out = sweep_with_progress([0.1 * i for i in range(1, 13)], _worker)
    print(f"completed {len(out)} cases")

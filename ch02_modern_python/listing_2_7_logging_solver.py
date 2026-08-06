"""Listing 2.7 -- A solver that reports progress through the logging module
instead of bare print statements.

Note: a *library* module should only ever call getLogger(__name__); deciding
where messages go (basicConfig) is the application's job, done here in __main__.

Python for Engineers and Scientists, Chapter 2.
Run:  python listing_2_7_logging_solver.py
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def _iterate(residual: float) -> float:
    """One solver sweep (stand-in): geometric residual decay."""
    return residual * 0.99


def solve(max_iter: int = 5000, tol: float = 1e-6,
          log_every: int = 1000) -> dict:
    logger.info("starting solve: max_iter=%d, tol=%.1e", max_iter, tol)
    residual = 1.0
    for it in range(max_iter):
        residual = _iterate(residual)
        if it % log_every == 0:
            logger.debug("iter %6d  residual %.3e", it, residual)
        if residual < tol:
            logger.info("converged in %d iterations (res=%.2e)", it, residual)
            return {"iterations": it, "residual": residual}
    logger.warning("did NOT converge: residual %.2e after %d iters",
                   residual, max_iter)
    return {"iterations": max_iter, "residual": residual}


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,                   # DEBUG lines stay hidden
        format="%(asctime)s  %(levelname)-8s  %(name)s: %(message)s",
    )
    print(solve())

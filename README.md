# Python for Engineers and Scientists — Companion Repository

Scientific Development, Numerical Modeling and Computational Simulation
by **I. L. Ferreira**

This repository holds the runnable source code for the book: three installable
domain packages (the Part IV case studies) and the per-chapter example listings.

## Contents

```
.
├── flowkit/                     # Chapter 22 — Fluid Mechanics package (installable)
│   └── src/flowkit/ ...         #   lid-driven cavity, verified vs Ghia (1982)
├── heatkit/                     # Chapter 23 — Heat Transfer package (installable)
│   └── src/heatkit/ ...         #   unified planar/cylindrical/spherical conduction
├── statistical-thermodynamics/  # Chapter 24 — Statistical Thermodynamics package
│   └── src/statistical_thermodynamics/ ...   # partition functions → properties, Monte Carlo
├── ch01_intro/ … ch29_ci/       # per-chapter runnable example listings
├── .github/workflows/tests.yml  # continuous integration (Chapter 29)
├── requirements.txt
├── LICENSE
└── README.md
```

Each of the three packages has its own `src/` layout, `pyproject.toml`, tests,
and README, and installs independently.

## Quick start

```bash
python3.12 -m venv .venv
source .venv/bin/activate           # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Install a package in editable mode and run its tests:
pip install -e ./flowkit[dev]                    && (cd flowkit && pytest)
pip install -e ./heatkit[dev]                    && (cd heatkit && pytest)
pip install -e ./statistical-thermodynamics[dev] && (cd statistical-thermodynamics && pytest)
```

## The three packages

| Package | Chapter | What it does | Verified against |
|---|---|---|---|
| `flowkit` | 22 | lid-driven cavity (vorticity–streamfunction) | Ghia et al. (1982), ~0.3 % |
| `heatkit` | 23 | unified planar/cylindrical/spherical conduction | exact analytical profiles |
| `statistical-thermodynamics` | 24 | partition functions → properties, Monte Carlo | experiment + compute-two-ways |

## Per-chapter examples

The `ch01_intro/` … `ch29_ci/` folders contain the book's listings, one folder
per chapter, each self-contained and runnable.

## License

MIT — see `LICENSE` and each package. The accompanying book text is © I. L. Ferreira.

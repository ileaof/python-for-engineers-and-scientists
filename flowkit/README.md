# flowkit

A small computational-fluid-dynamics package accompanying *Python for Engineers
and Scientists* (Chapter 22). It solves the **lid-driven cavity** by the
vorticity–streamfunction method and verifies the result against the benchmark of
Ghia, Ghia & Shin (1982).

## Install

```bash
pip install -e ".[dev]"
```

## Use

```python
from flowkit.cavity import solve_cavity
from flowkit.benchmarks import cavity_centreline_error

result = solve_cavity(n=64, reynolds=100.0)
print("centreline error vs Ghia:", cavity_centreline_error(result))
```

On a 64×64 grid at Re = 100 the maximum centreline error is about 0.3 %.

## Test

```bash
pytest
```

## Layout

```
flowkit/
├── pyproject.toml
├── src/flowkit/
│   ├── __init__.py
│   ├── mesh.py
│   ├── poisson.py       # streamfunction Poisson solver
│   ├── cavity.py        # vorticity-streamfunction cavity solver
│   └── benchmarks.py    # Ghia et al. (1982) data + comparison
└── tests/test_cavity.py
```

MIT License.

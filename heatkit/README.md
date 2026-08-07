# heatkit

A unified heat-conduction package accompanying *Python for Engineers and
Scientists* (Chapter 23). A single finite-volume solver handles **planar
(m=0), cylindrical (m=1) and spherical (m=2)** geometry via face areas
A ~ r**m, verified against exact analytical profiles, plus an unconditionally
stable implicit transient solver.

## Install

```bash
pip install -e ".[dev]"
```

`scipy` is optional: if present it is used for the banded solve, otherwise a
built-in Thomas algorithm is used, so the package works with NumPy alone.

## Use

```python
from heatkit.mesh import RadialMesh
from heatkit.conduction import solve_conduction

mesh = RadialMesh(r0=1.0, r1=2.0, n=40)
T = solve_conduction(mesh, k=1.0, m=1, T_left=100.0, T_right=0.0)  # cylindrical
```

The planar case (m=0) reproduces the exact linear profile to round-off.

## Test

```bash
pytest
```

## Layout

```
heatkit/
├── pyproject.toml
├── src/heatkit/
│   ├── __init__.py
│   ├── mesh.py
│   ├── conduction.py    # unified A~r^m steady solver
│   ├── analytical.py    # exact profiles for verification
│   └── transient.py     # implicit (backward-Euler) transient step
└── tests/test_conduction.py
```

MIT License.

# Listing 8.1 — The anatomy of a scientific package (src layout)

Reference structure used throughout Part IV. Dependencies flow strictly
downward (see Listing 8.2 for the `__init__.py`).

```
statistical-thermodynamics/
├── pyproject.toml                    # build metadata, deps, tool config
├── README.md                         # what it is, how to install and use
├── LICENSE
├── src/
│   └── statistical_thermodynamics/   # THE importable package
│       ├── __init__.py               # public API + version
│       ├── constants.py              # leaf: depends on nothing
│       ├── partition_functions.py    # depends on constants
│       ├── thermodynamics.py         # depends on partition_functions
│       ├── kinetic_theory.py
│       ├── quantum_statistics.py
│       ├── numerical_methods.py      # Metropolis, autocorrelation, bootstrap
│       └── plotting.py               # shared figure style
├── tests/                            # mirrors the package, one file per module
│   ├── test_constants.py
│   ├── test_partition_functions.py
│   └── test_thermodynamics.py
└── tools/                            # scripts: build figures, run examples
    ├── run_all_examples.py
    └── build_all_figures.py
```

## Layering (dependencies point downward only, never in a cycle)

| Layer            | Example modules                     | Depends on            |
|------------------|-------------------------------------|-----------------------|
| Foundations      | constants, utilities                | (nothing — leaves)    |
| Physics kernels  | partition_functions, potentials     | foundations           |
| Derived physics  | thermodynamics, quantum_statistics  | kernels + foundations |
| Numerics         | numerical_methods                   | foundations           |
| Presentation     | plotting                            | foundations           |
| Applications     | tools/, examples                    | everything below      |

## Install (editable), then test against the installed package

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e .
pytest
```

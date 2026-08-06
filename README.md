# Python for Engineers and Scientists — Companion Code

> **Scientific Development, Numerical Modeling and Computational Simulation**
> by **I. L. Ferreira** · [ileao@ufpa.br](mailto:ileao@ufpa.br)

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.26%2B-013243?logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-1.11%2B-8CAAE6?logo=scipy&logoColor=white)
![Style](https://img.shields.io/badge/style-PEP%208-informational)
![License](https://img.shields.io/badge/license-MIT-green)

The complete, runnable source code for every listing in the book — **70 Python
scripts across 24 chapters**, plus reference configuration files. Each listing is
self-contained, follows PEP 8, uses type hints where they teach something, and
runs directly from the command line with no project setup beyond the scientific
stack.

---

## Table of contents

- [About this code](#about-this-code)
- [Quick start](#quick-start)
- [How the examples are organized](#how-the-examples-are-organized)
- [Running an example](#running-an-example)
- [Requirements](#requirements)
- [Book map & listing index](#book-map--listing-index)
  - [Part I — Foundations](#part-i--foundations)
  - [Part II — The scientific stack](#part-ii--the-scientific-stack)
  - [Part III — Software engineering](#part-iii--software-engineering)
  - [Part IV — Numerical methods](#part-iv--numerical-methods)
  - [Part V — High-performance Python](#part-v--high-performance-python)
  - [Part VI — Interfaces & scientific I/O](#part-vi--interfaces--scientific-io)
  - [Part VII — Testing, packaging & tooling](#part-vii--testing-packaging--tooling)
  - [Part VIII — Verified case studies](#part-viii--verified-case-studies)
- [Verification at a glance](#verification-at-a-glance)
- [Citing this work](#citing-this-work)
- [License](#license)

---

## About this code

The book teaches computational science as an engineering discipline, and this
repository is written to match. Three habits run through every listing:

- **Verify twice.** Wherever there is a closed form, the code also computes the
  quantity a second, independent way (a numerical integral, a benchmark table, a
  refined grid) and reports the difference. Trust is earned, not assumed.
- **Readable first, fast second.** Kernels are written clearly, then the
  performance chapters show the same physics accelerated with vectorization,
  Numba, and parallelism — so you can see exactly what speed costs in clarity.
- **Physically grounded.** Examples are drawn from real engineering and science:
  Maxwell–Boltzmann kinetics, heat conduction, the lid-driven cavity, radiative
  balance, partition functions — not toy problems.

---

## Quick start

```bash
# 1. Clone
git clone https://github.com/ileaof/python-for-engineers-and-scientists.git
cd python-for-engineers-and-scientists

# 2. Create an isolated environment (Python 3.12+)
python3.12 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 3. Install the scientific stack
pip install -r requirements.txt

# 4. Run any listing
python ch01_intro/listing_1_4_verify_two_ways.py
```

Expected output from the last command:

```
closed form  <v> =   476.2619 m/s
numerical    <v> =   476.2619 m/s
relative error   = 2.39e-16
```

---

## How the examples are organized

Files are grouped one directory per chapter (`chNN_topic/`) and named after the
listing they correspond to in the book:

```
listing_<chapter>_<number>_<slug>.py
        └ 4       └ 8      └ jacobi_laplace
```

Every script carries the same header — a one-line summary, the chapter it belongs
to, and the exact command to run it — so any file is understandable on its own:

```python
"""Listing 4.8 -- A Jacobi solver for the 2-D Laplace equation ...

Python for Engineers and Scientists, Chapter 4.
Run:  python listing_4_8_jacobi_laplace.py
"""
```

Repository layout:

```
.
├── ch01_intro/                   Introduction to Scientific Python
├── ch02_modern_python/           Modern Python Programming
├── ch03_data_structures/         Data Structures
├── ch04_numpy/                   NumPy in Depth
├── ch05_scipy/                   SciPy for Engineering
├── ch06_visualization/           Scientific Visualization
├── ch07_oop/                     Object-Oriented Programming
├── ch08_architecture/            Architecture of Large Projects
├── ch09_numerical_methods/       Numerical Methods
├── ch10_linear_algebra/          Computational Linear Algebra
├── ch11_differential_equations/  Differential Equations
├── ch12_integration/             Numerical Integration
├── ch13_optimization/            Optimization
├── ch14_interpolation/           Interpolation
├── ch15_parallel/                Parallel Programming
├── ch16_numba/                   Just-in-Time Compilation with Numba
├── ch17_vectorized/              Vectorized Computing
├── ch18_pyqt6/                   Graphical Interfaces with PyQt6
├── ch19_files/                   Reading and Writing Scientific Files
├── ch20_testing/                 Automated Testing
├── ch21_libraries/               Developing Scientific Libraries
├── ch22_fluid_mechanics/         Case study — lid-driven cavity
├── ch23_heat_transfer/           Case study — steady conduction
├── ch24_statistical_thermo/      Case study — statistical thermodynamics
├── ch28_git/                     Version control (pre-commit reference)
├── ch29_ci/                      Continuous integration (GitHub Actions reference)
├── requirements.txt
└── README.md
```

> **Not in this repository:** Chapters 25–27 and 30 (best practices, publishing
> to PyPI, documentation with Sphinx, and the capstone) are discussed in the book
> as commands and prose rather than standalone scripts. Chapters 28–29 ship only
> the reference configuration files shown above.

---

## Running an example

Every file runs on its own:

```bash
python ch01_intro/listing_1_4_verify_two_ways.py
python ch04_numpy/listing_4_8_jacobi_laplace.py
python ch22_fluid_mechanics/cavity.py
```

**Visualization (Chapter 6).** The plotting scripts import the shared style
module [`plotting.py`](ch06_visualization/plotting.py), so run them from inside
their folder (or add it to `PYTHONPATH`):

```bash
cd ch06_visualization
python listing_6_3_convergence_plot.py     # writes convergence.png
python listing_6_4_field_plot.py           # writes field.png
```

**Tests (Chapter 20).** The test suite runs under pytest:

```bash
pytest ch20_testing/test_examples.py -v
```

---

## Requirements

**Python 3.12 or newer.** Install everything at once with
`pip install -r requirements.txt`, or add packages only as the chapters you read
require them.

| Package        | Minimum  | Required by                          | Purpose                                   |
|----------------|----------|--------------------------------------|-------------------------------------------|
| **numpy**      | 1.26     | all chapters                         | arrays, vectorization, linear algebra     |
| **scipy**      | 1.11     | Ch 5, 11–14, 23                      | integration, solvers, special functions   |
| **matplotlib** | 3.8      | Ch 6, 18                             | scientific plotting                       |
| **pandas**     | 2.1      | Ch 3                                 | tabular data (convergence tables)         |
| numba          | 0.59     | Ch 16, 17                            | JIT-compiled and parallel kernels         |
| tqdm           | 4.66     | Ch 15                                | progress bars for long sweeps             |
| h5py           | 3.10     | Ch 19                                | self-describing HDF5 I/O                  |
| meshio         | 5.3      | Ch 19                                | mesh I/O (VTK / ParaView)                 |
| PyQt6          | 6.6      | Ch 18                                | desktop GUI front end                     |
| pytest         | 7.4      | Ch 20                                | test runner                               |

---

## Book map & listing index

The book is organized into eight parts. Each section below lists its chapters,
the concepts they cover, and every runnable listing.

### Part I — Foundations

*Getting productive: the scientific mindset, modern Python idioms, and the data
structures numerical work is built on.*

| Listing | File | Topic |
|---|---|---|
| 1.2 | [listing_1_2_speeds_throwaway.py](ch01_intro/listing_1_2_speeds_throwaway.py) | throwaway script |
| 1.3 | [listing_1_3_characteristic_speeds.py](ch01_intro/listing_1_3_characteristic_speeds.py) | reusable function |
| 1.4 | [listing_1_4_verify_two_ways.py](ch01_intro/listing_1_4_verify_two_ways.py) | verification by two routes |
| 2.2 | [listing_2_2_type_hints.py](ch02_modern_python/listing_2_2_type_hints.py) | type hints |
| 2.3 | [listing_2_3_fluid_properties.py](ch02_modern_python/listing_2_3_fluid_properties.py) | frozen dataclass |
| 2.4 | [listing_2_4_simulation_config.py](ch02_modern_python/listing_2_4_simulation_config.py) | config dataclass |
| 2.7 | [listing_2_7_logging_solver.py](ch02_modern_python/listing_2_7_logging_solver.py) | logging |
| 3.1 | [listing_3_1_builtins.py](ch03_data_structures/listing_3_1_builtins.py) | built-in containers |
| 3.2 | [listing_3_2_list_vs_array.py](ch03_data_structures/listing_3_2_list_vs_array.py) | list vs array |
| 3.3 | [listing_3_3_array_basics.py](ch03_data_structures/listing_3_3_array_basics.py) | array anatomy |
| 3.4 | [listing_3_4_mesh1d.py](ch03_data_structures/listing_3_4_mesh1d.py) | 1-D finite-volume mesh |
| 3.5 | [listing_3_5_structured_array.py](ch03_data_structures/listing_3_5_structured_array.py) | structured array |
| 3.6 | [listing_3_6_convergence_dataframe.py](ch03_data_structures/listing_3_6_convergence_dataframe.py) | convergence table |

### Part II — The scientific stack

*NumPy, SciPy, and Matplotlib — the three libraries every example rests on.*

| Listing | File | Topic |
|---|---|---|
| 4.1 | [listing_4_1_vectorization.py](ch04_numpy/listing_4_1_vectorization.py) | vectorization |
| 4.2 | [listing_4_2_heat_capacity.py](ch04_numpy/listing_4_2_heat_capacity.py) | numerically stable ufunc |
| 4.3 | [listing_4_3_broadcasting.py](ch04_numpy/listing_4_3_broadcasting.py) | broadcasting |
| 4.4 | [listing_4_4_views_copies.py](ch04_numpy/listing_4_4_views_copies.py) | views vs copies |
| 4.5, 4.6 | [listing_4_5_4_6_stencils.py](ch04_numpy/listing_4_5_4_6_stencils.py) | 1-D / 2-D Laplacian stencils |
| 4.7 | [listing_4_7_reductions.py](ch04_numpy/listing_4_7_reductions.py) | reductions and `axis` |
| 4.8 | [listing_4_8_jacobi_laplace.py](ch04_numpy/listing_4_8_jacobi_laplace.py) | Jacobi Laplace solver |
| 5.1 | [listing_5_1_tridiagonal.py](ch05_scipy/listing_5_1_tridiagonal.py) | banded (tridiagonal) solver |
| 5.2 | [listing_5_2_mean_speed_quad.py](ch05_scipy/listing_5_2_mean_speed_quad.py) | adaptive quadrature |
| 5.3 | [listing_5_3_radiative_balance.py](ch05_scipy/listing_5_3_radiative_balance.py) | `brentq` root finding |
| 5.4 | [listing_5_4_interpolation.py](ch05_scipy/listing_5_4_interpolation.py) | cubic spline |
| 5.5 | [listing_5_5_special_functions.py](ch05_scipy/listing_5_5_special_functions.py) | special functions (`erfc`, `zeta`) |
| 6.1 | [listing_6_1_oo_interface.py](ch06_visualization/listing_6_1_oo_interface.py) | object-oriented interface |
| 6.2 | [plotting.py](ch06_visualization/plotting.py) | shared publication style module |
| 6.3 | [listing_6_3_convergence_plot.py](ch06_visualization/listing_6_3_convergence_plot.py) | convergence plot |
| 6.4 | [listing_6_4_field_plot.py](ch06_visualization/listing_6_4_field_plot.py) | 2-D field plot |

### Part III — Software engineering

*Structuring code that grows: encapsulation, composition, polymorphism,
protocols, and the anatomy of a well-layered package.*

| Listing | File | Topic |
|---|---|---|
| 7.2, 7.3 | [listing_7_2_7_3_reservoir_network.py](ch07_oop/listing_7_2_7_3_reservoir_network.py) | encapsulation + composition |
| 7.4 | [listing_7_4_boundary_conditions.py](ch07_oop/listing_7_4_boundary_conditions.py) | inheritance / polymorphism |
| 7.5 | [listing_7_5_solver_protocol.py](ch07_oop/listing_7_5_solver_protocol.py) | protocols (structural typing) |
| 8.1 | [listing_8_1_package_layout.md](ch08_architecture/listing_8_1_package_layout.md) | `src` layout + layering |
| 8.2 | [listing_8_2_package_init.py](ch08_architecture/listing_8_2_package_init.py) | curated public API |

### Part IV — Numerical methods

*The core of the book: floating-point reality, linear systems, ODEs and PDEs,
integration, optimization, and interpolation — each verified against theory.*

| Listing | File | Topic |
|---|---|---|
| 9.1, 9.2 | [listing_9_1_9_2_floating_point.py](ch09_numerical_methods/listing_9_1_9_2_floating_point.py) | machine epsilon, conditioning |
| 9.3 | [listing_9_3_verification_tools.py](ch09_numerical_methods/listing_9_3_verification_tools.py) | observed order, Richardson, GCI |
| 10.1, 10.4 | [listing_10_1_10_4_direct_and_cg.py](ch10_linear_algebra/listing_10_1_10_4_direct_and_cg.py) | direct solve + conjugate gradient |
| 10.2 | [listing_10_2_poisson_2d.py](ch10_linear_algebra/listing_10_2_poisson_2d.py) | sparse 2-D Poisson |
| 10.3 | [listing_10_3_sor_laplace.py](ch10_linear_algebra/listing_10_3_sor_laplace.py) | SOR iteration |
| 11.1, 11.2 | [listing_11_1_11_2_ode.py](ch11_differential_equations/listing_11_1_11_2_ode.py) | Euler + `solve_ivp` |
| 11.3 | [listing_11_3_heat_explicit.py](ch11_differential_equations/listing_11_3_heat_explicit.py) | explicit heat equation (FTCS) |
| 12.1 | [listing_12_1_newton_cotes.py](ch12_integration/listing_12_1_newton_cotes.py) | trapezoid vs Simpson |
| 12.2 | [listing_12_2_gauss_legendre.py](ch12_integration/listing_12_2_gauss_legendre.py) | Gauss–Legendre quadrature |
| 12.3 | [listing_12_3_adaptive_quad.py](ch12_integration/listing_12_3_adaptive_quad.py) | adaptive quadrature (virial) |
| 12.4 | [listing_12_4_partition_sum.py](ch12_integration/listing_12_4_partition_sum.py) | series sum vs closed form |
| 13.1 | [listing_13_1_root_finding.py](ch13_optimization/listing_13_1_root_finding.py) | `brentq` balance |
| 13.2 | [listing_13_2_nonlinear_system.py](ch13_optimization/listing_13_2_nonlinear_system.py) | nonlinear system (`root`) |
| 13.3 | [listing_13_3_minimization.py](ch13_optimization/listing_13_3_minimization.py) | minimization (LJ, Rosenbrock) |
| 13.4 | [listing_13_4_curve_fit.py](ch13_optimization/listing_13_4_curve_fit.py) | `curve_fit` + uncertainties |
| 14.1 | [listing_14_1_linear_table.py](ch14_interpolation/listing_14_1_linear_table.py) | linear table lookup |
| 14.2 | [listing_14_2_runge.py](ch14_interpolation/listing_14_2_runge.py) | Runge phenomenon |
| 14.3 | [listing_14_3_cubic_spline.py](ch14_interpolation/listing_14_3_cubic_spline.py) | cubic spline |
| 14.4 | [listing_14_4_regular_grid.py](ch14_interpolation/listing_14_4_regular_grid.py) | 2-D grid interpolation |

### Part V — High-performance Python

*The same kernels, made fast: multiprocessing sweeps, JIT compilation with
Numba, and a step-by-step vectorization ladder.*

| Listing | File | Topic |
|---|---|---|
| 15.1 | [listing_15_1_parameter_sweep.py](ch15_parallel/listing_15_1_parameter_sweep.py) | parallel parameter sweep |
| 15.2 | [listing_15_2_parallel_monte_carlo.py](ch15_parallel/listing_15_2_parallel_monte_carlo.py) | parallel Monte Carlo (spawn) |
| 15.3 | [listing_15_3_tqdm_progress.py](ch15_parallel/listing_15_3_tqdm_progress.py) | parallel + tqdm progress |
| 16.1 | [listing_16_1_jit_recurrence.py](ch16_numba/listing_16_1_jit_recurrence.py) | `@njit` recurrence |
| 16.2 | [listing_16_2_metropolis_njit.py](ch16_numba/listing_16_2_metropolis_njit.py) | compiled Metropolis sampler |
| 16.3 | [listing_16_3_parallel_stencil.py](ch16_numba/listing_16_3_parallel_stencil.py) | `prange` parallel stencil |
| 17.1 | [listing_17_1_four_ways.py](ch17_vectorized/listing_17_1_four_ways.py) | one kernel, four ways |
| 17.2 | [listing_17_2_memory_aware.py](ch17_vectorized/listing_17_2_memory_aware.py) | in-place / `out=` memory reuse |

### Part VI — Interfaces & scientific I/O

*Getting data and results in and out: a responsive desktop GUI, and the file
formats that make results portable and self-describing.*

| Listing | File | Topic |
|---|---|---|
| 18.1–18.5 | [solver_gui.py](ch18_pyqt6/solver_gui.py) | threaded PyQt6 solver front end |
| 19.1 | [listing_19_1_numpy_csv.py](ch19_files/listing_19_1_numpy_csv.py) | `.npy` / `.npz` / CSV |
| 19.2 | [listing_19_2_hdf5.py](ch19_files/listing_19_2_hdf5.py) | self-describing HDF5 |
| 19.3 | [listing_19_3_meshio.py](ch19_files/listing_19_3_meshio.py) | mesh I/O (VTK / ParaView) |
| 19.4 | [listing_19_4_tecplot.py](ch19_files/listing_19_4_tecplot.py) | Tecplot ASCII export |

### Part VII — Testing, packaging & tooling

*Turning scripts into trustworthy, shareable software: automated tests,
packaging metadata, version-control hooks, and continuous integration.*

| Listing | File | Topic |
|---|---|---|
| 20.1–20.3 | [test_examples.py](ch20_testing/test_examples.py) | pytest suite — tolerances, fixtures, parametrization |
| 21.1, 21.3 | [listing_21_1_pyproject.toml](ch21_libraries/listing_21_1_pyproject.toml) | packaging metadata reference |
| 28.4 | [pre-commit-config.yaml](ch28_git/pre-commit-config.yaml) | pre-commit hooks (Black, lint) |
| 29.1 | [.github/workflows/tests.yml](ch29_ci/.github/workflows/tests.yml) | GitHub Actions test matrix |

### Part VIII — Verified case studies

*Three complete solvers that put the whole book to work — each checked against an
analytical solution or a published benchmark.*

| Chapter | File | What it does |
|---|---|---|
| 22 | [cavity.py](ch22_fluid_mechanics/cavity.py) | lid-driven cavity (vorticity–streamfunction), verified vs Ghia et al. (1982) |
| 22 | [cavity_verify.py](ch22_fluid_mechanics/cavity_verify.py) | compact one-file verification of the cavity result |
| 23 | [conduction.py](ch23_heat_transfer/conduction.py) | unified planar / cylindrical / spherical finite-volume conduction |
| 24 | [partition_and_error.py](ch24_statistical_thermo/partition_and_error.py) | partition function two ways + Monte-Carlo blocking error |

---

## Verification at a glance

Because the book insists on checking results, several listings print an error
against a known answer. Running them reproduces these figures:

| Example | Check | Result |
|---|---|---|
| Ch 1 — mean molecular speed | closed form vs numerical integral | relative error ≈ 2 × 10⁻¹⁶ |
| Ch 22 — lid-driven cavity | centreline `u` vs Ghia (Re = 100, 64² grid) | max error ≈ 0.28 % |
| Ch 23 — steady conduction | FVM vs exact profile (all three geometries) | max error ≈ machine precision |
| Ch 9 — verification tools | observed order of accuracy | recovers the theoretical order |

---

## Citing this work

If this material supports your teaching or research, please cite the book:

```bibtex
@book{ferreira_python_engineers_scientists_2026,
  author    = {Ferreira, I. L.},
  title     = {Python for Engineers and Scientists: Scientific Development,
               Numerical Modeling and Computational Simulation},
  year      = {2026},
  publisher = {Kindle Direct Publishing (Amazon KDP)},
  note      = {Companion code: https://github.com/ileaof/python-for-engineers-and-scientists}
}
```

---

## License

Released under the **MIT License** — see the book's front matter. You are free to
use, modify, and share the code, including in teaching and research, with
attribution.

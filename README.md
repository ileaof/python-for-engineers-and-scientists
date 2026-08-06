# Python for Engineers and Scientists — Companion Code

Scientific Development, Numerical Modeling and Computational Simulation
by I. L. Ferreira

This repository holds the runnable source code for every listing in the book,
organized by chapter. Each file is self-contained, follows PEP 8, uses type
hints where instructive, and can be run directly from the command line.

## Requirements

Python 3.12+ and the scientific stack:

```bash
python3.12 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Layout

```
code/
├── ch01_intro/                Introduction to Scientific Python
├── ch02_modern_python/        Modern Python Programming
├── ch03_data_structures/      Data Structures
├── ch04_numpy/                NumPy in Depth
├── ch05_scipy/                SciPy for Engineering
├── ch06_visualization/        Scientific Visualization
├── ch07_oop/                  Object-Oriented Programming
├── ch08_architecture/         Architecture of Large Projects
├── ch09_numerical_methods/    Numerical Methods
├── ch10_linear_algebra/       Computational Linear Algebra
├── ch11_differential_equations/  Differential Equations
├── ch12_integration/          Numerical Integration
├── ch13_optimization/         Optimization
├── ch14_interpolation/        Interpolation
├── ch15_parallel/             Parallel Programming
├── ch16_numba/                Numba
├── ch17_vectorized/           Vectorized Computing
├── ch18_pyqt6/                Graphical Interfaces with PyQt6
├── ch19_files/                Reading and Writing Scientific Files
├── ch20_testing/              Automated Testing
├── ch21_libraries/            Developing Scientific Libraries
├── ch22_fluid_mechanics/      Project 1: Fluid Mechanics package (cavity)
├── ch23_heat_transfer/        Project 2: Heat Transfer package (conduction)
├── ch24_statistical_thermo/   Project 3: Statistical Thermodynamics package
├── ch28_git/                  pre-commit config reference
├── ch29_ci/                   GitHub Actions workflow reference
├── requirements.txt
└── README.md

Chapters 25-27 and 30 are practice/architecture chapters (best practices, PyPI,
Sphinx, capstone); their listings are commands and configuration shown inline in
the book. Chapters 28-29 include the reference config files above.
```

Later blocks (Chapters 7–30) are added as they are written.

## Running an example

Every file runs on its own, for example:

```bash
python ch01_intro/listing_1_4_verify_two_ways.py
python ch04_numpy/listing_4_8_jacobi_laplace.py
```

The Chapter 6 plotting scripts import the shared style module `plotting.py`, so
run them from inside `ch06_visualization/` (or add that folder to `PYTHONPATH`):

```bash
cd ch06_visualization
python listing_6_3_convergence_plot.py     # writes convergence.png
python listing_6_4_field_plot.py           # writes field.png
```

## Listing index

| Listing | File | Topic |
|---|---|---|
| 1.2 | ch01_intro/listing_1_2_speeds_throwaway.py | throwaway script |
| 1.3 | ch01_intro/listing_1_3_characteristic_speeds.py | reusable function |
| 1.4 | ch01_intro/listing_1_4_verify_two_ways.py | verify two ways |
| 2.2 | ch02_modern_python/listing_2_2_type_hints.py | type hints |
| 2.3 | ch02_modern_python/listing_2_3_fluid_properties.py | frozen dataclass |
| 2.4 | ch02_modern_python/listing_2_4_simulation_config.py | config dataclass |
| 2.7 | ch02_modern_python/listing_2_7_logging_solver.py | logging |
| 3.1 | ch03_data_structures/listing_3_1_builtins.py | built-in containers |
| 3.2 | ch03_data_structures/listing_3_2_list_vs_array.py | list vs array |
| 3.3 | ch03_data_structures/listing_3_3_array_basics.py | array anatomy |
| 3.4 | ch03_data_structures/listing_3_4_mesh1d.py | 1-D FV mesh |
| 3.5 | ch03_data_structures/listing_3_5_structured_array.py | structured array |
| 3.6 | ch03_data_structures/listing_3_6_convergence_dataframe.py | convergence table |
| 4.1 | ch04_numpy/listing_4_1_vectorization.py | vectorization |
| 4.2 | ch04_numpy/listing_4_2_heat_capacity.py | stable ufunc |
| 4.3 | ch04_numpy/listing_4_3_broadcasting.py | broadcasting |
| 4.4 | ch04_numpy/listing_4_4_views_copies.py | views vs copies |
| 4.5, 4.6 | ch04_numpy/listing_4_5_4_6_stencils.py | 1-D/2-D Laplacian stencils |
| 4.7 | ch04_numpy/listing_4_7_reductions.py | reductions and axis |
| 4.8 | ch04_numpy/listing_4_8_jacobi_laplace.py | Jacobi Laplace solver |
| 5.1 | ch05_scipy/listing_5_1_tridiagonal.py | banded solver |
| 5.2 | ch05_scipy/listing_5_2_mean_speed_quad.py | adaptive quadrature |
| 5.3 | ch05_scipy/listing_5_3_radiative_balance.py | brentq root finding |
| 5.4 | ch05_scipy/listing_5_4_interpolation.py | cubic spline |
| 5.5 | ch05_scipy/listing_5_5_special_functions.py | erfc, zeta |
| 6.1 | ch06_visualization/listing_6_1_oo_interface.py | OO interface |
| 6.2 | ch06_visualization/plotting.py | shared style module |
| 6.3 | ch06_visualization/listing_6_3_convergence_plot.py | convergence plot |
| 6.4 | ch06_visualization/listing_6_4_field_plot.py | 2-D field plot |
| 7.2, 7.3 | ch07_oop/listing_7_2_7_3_reservoir_network.py | encapsulation + composition |
| 7.4 | ch07_oop/listing_7_4_boundary_conditions.py | inheritance / polymorphism |
| 7.5 | ch07_oop/listing_7_5_solver_protocol.py | protocols (structural typing) |
| 8.1 | ch08_architecture/listing_8_1_package_layout.md | src layout + layering |
| 8.2 | ch08_architecture/listing_8_2_package_init.py | curated public API |
| 9.1, 9.2 | ch09_numerical_methods/listing_9_1_9_2_floating_point.py | epsilon, conditioning |
| 9.3 | ch09_numerical_methods/listing_9_3_verification_tools.py | order, Richardson, GCI |
| 10.1, 10.4 | ch10_linear_algebra/listing_10_1_10_4_direct_and_cg.py | direct + conjugate gradient |
| 10.2 | ch10_linear_algebra/listing_10_2_poisson_2d.py | sparse 2-D Poisson |
| 10.3 | ch10_linear_algebra/listing_10_3_sor_laplace.py | SOR iteration |
| 11.1, 11.2 | ch11_differential_equations/listing_11_1_11_2_ode.py | Euler + solve_ivp |
| 11.3 | ch11_differential_equations/listing_11_3_heat_explicit.py | explicit heat (FTCS) |
| 12.1 | ch12_integration/listing_12_1_newton_cotes.py | trapezoid vs Simpson |
| 12.2 | ch12_integration/listing_12_2_gauss_legendre.py | Gauss-Legendre quadrature |
| 12.3 | ch12_integration/listing_12_3_adaptive_quad.py | adaptive quad (virial) |
| 12.4 | ch12_integration/listing_12_4_partition_sum.py | sum vs closed form |
| 13.1 | ch13_optimization/listing_13_1_root_finding.py | brentq balance |
| 13.2 | ch13_optimization/listing_13_2_nonlinear_system.py | nonlinear system (root) |
| 13.3 | ch13_optimization/listing_13_3_minimization.py | minimize (LJ, Rosenbrock) |
| 13.4 | ch13_optimization/listing_13_4_curve_fit.py | curve_fit + uncertainties |
| 14.1 | ch14_interpolation/listing_14_1_linear_table.py | linear table lookup |
| 14.2 | ch14_interpolation/listing_14_2_runge.py | Runge phenomenon |
| 14.3 | ch14_interpolation/listing_14_3_cubic_spline.py | cubic spline |
| 14.4 | ch14_interpolation/listing_14_4_regular_grid.py | 2-D grid interpolation |
| 15.1 | ch15_parallel/listing_15_1_parameter_sweep.py | parallel parameter sweep |
| 15.2 | ch15_parallel/listing_15_2_parallel_monte_carlo.py | parallel Monte Carlo (spawn) |
| 15.3 | ch15_parallel/listing_15_3_tqdm_progress.py | parallel + tqdm progress |
| 16.1 | ch16_numba/listing_16_1_jit_recurrence.py | @njit recurrence |
| 16.2 | ch16_numba/listing_16_2_metropolis_njit.py | compiled Metropolis |
| 16.3 | ch16_numba/listing_16_3_parallel_stencil.py | prange parallel stencil |
| 17.1 | ch17_vectorized/listing_17_1_four_ways.py | four-way performance ladder |
| 17.2 | ch17_vectorized/listing_17_2_memory_aware.py | in-place / out= memory |

| 18 | ch18_pyqt6/solver_gui.py | PyQt6 solver front end (threaded) |
| 19.1 | ch19_files/listing_19_1_numpy_csv.py | npy/npz/CSV |
| 19.2 | ch19_files/listing_19_2_hdf5.py | self-describing HDF5 |
| 19.3 | ch19_files/listing_19_3_meshio.py | mesh I/O (VTK/ParaView) |
| 19.4 | ch19_files/listing_19_4_tecplot.py | Tecplot ASCII export |
| 20 | ch20_testing/test_examples.py | pytest suite (run: `pytest -v`) |
| 21.1 | ch21_libraries/listing_21_1_pyproject.toml | packaging metadata reference |
| 22 | ch22_fluid_mechanics/cavity.py | lid-driven cavity, verified vs Ghia (0.28%) |
| 23 | ch23_heat_transfer/conduction.py | unified planar/cylindrical/spherical FVM |
| 24 | ch24_statistical_thermo/partition_and_error.py | partition two-ways + blocking error |

Note: Ch16-17 need `numba`; Ch18 needs `PyQt6`; Ch19 needs `h5py`/`meshio`;
Ch20 needs `pytest`.

## License

MIT (see the book's front matter).

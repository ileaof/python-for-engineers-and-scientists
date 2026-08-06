"""Listing 3.2 -- The same sum, two orders of magnitude apart.

Python for Engineers and Scientists, Chapter 3.
Run:  python listing_3_2_list_vs_array.py
"""

import time

import numpy as np

n = 1_000_000
py_list = list(range(n))
np_arr = np.arange(n, dtype=np.float64)

# Pure Python: a million interpreted iterations
t0 = time.perf_counter()
total = 0.0
for x in py_list:
    total += x
t_py = time.perf_counter() - t0

# NumPy: one call into compiled code over a contiguous buffer
t0 = time.perf_counter()
total = np_arr.sum()
t_np = time.perf_counter() - t0


if __name__ == "__main__":
    print(f"python loop : {t_py*1e3:8.2f} ms")
    print(f"numpy sum   : {t_np*1e3:8.2f} ms")
    print(f"speed-up    : {t_py/t_np:8.1f}x")

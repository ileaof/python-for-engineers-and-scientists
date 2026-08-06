"""Listing 3.6 -- A convergence study as a DataFrame; the observed order of
accuracy computed column-wise.

Python for Engineers and Scientists, Chapter 3.
Run:  python listing_3_6_convergence_dataframe.py
"""

import numpy as np
import pandas as pd

# A grid-convergence study: error and cost versus mesh size
grids = np.array([16, 32, 64, 128, 256])
h = 1.0 / grids
l2_error = 0.85 * h**2                    # a second-order method

study = pd.DataFrame({
    "N": grids,
    "h": h,
    "L2_error": l2_error,
})

# Observed order p from successive refinements: p = log2(e_coarse / e_fine)
study["order"] = np.log2(study["L2_error"].shift() / study["L2_error"])


if __name__ == "__main__":
    print(study.to_string(index=False,
                          float_format=lambda v: f"{v:.4e}"))

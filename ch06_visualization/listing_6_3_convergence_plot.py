"""Listing 6.3 -- A convergence study rendered through the shared style; the
log-log slope IS the verification of the order of accuracy.

Python for Engineers and Scientists, Chapter 6.
Run:  python listing_6_3_convergence_plot.py   (writes convergence.png)
"""

import matplotlib
matplotlib.use("Agg")

import numpy as np

from plotting import new_figure, COLORS

grids = np.array([16, 32, 64, 128, 256])
h = 1.0 / grids
error = 0.85 * h**2                      # a second-order method's error

fig, ax = new_figure()
ax.loglog(h, error, "o-", color=COLORS["navy"], label="measured L2 error")
ax.loglog(h, error[0] * (h / h[0])**2, "--",
          color=COLORS["grey"], label="slope 2 (theory)")
ax.set_xlabel(r"mesh spacing $h$")
ax.set_ylabel(r"$\|e\|_2$")
ax.set_title("Observed order of accuracy")
ax.legend()
fig.savefig("convergence.png")

if __name__ == "__main__":
    slope = np.polyfit(np.log(h), np.log(error), 1)[0]
    print(f"measured log-log slope = {slope:.3f} (expect 2.0); wrote convergence.png")

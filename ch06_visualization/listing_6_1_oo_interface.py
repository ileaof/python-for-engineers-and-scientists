"""Listing 6.1 -- The object-oriented interface: explicit Figure, Axes, Artists.

Python for Engineers and Scientists, Chapter 6.
Run:  python listing_6_1_oo_interface.py   (writes trig.png)
"""

import matplotlib
matplotlib.use("Agg")            # non-interactive backend for scripts

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0, 2.0 * np.pi, 200)

fig, ax = plt.subplots(figsize=(6, 4))     # explicit Figure and Axes
ax.plot(x, np.sin(x), label="sin")
ax.plot(x, np.cos(x), label="cos")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("The object-oriented interface")
ax.legend()
fig.savefig("trig.png", dpi=200, bbox_inches="tight")

if __name__ == "__main__":
    print("wrote trig.png")

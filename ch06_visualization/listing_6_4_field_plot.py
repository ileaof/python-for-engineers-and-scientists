"""Listing 6.4 -- A 2-D field: filled colour map, overlaid contours, colourbar,
equal aspect. The analytical Laplace solution on the unit square.

Python for Engineers and Scientists, Chapter 6.
Run:  python listing_6_4_field_plot.py   (writes field.png)
"""

import matplotlib
matplotlib.use("Agg")

import numpy as np

from plotting import new_figure

n = 80
x = np.linspace(0.0, 1.0, n)
y = np.linspace(0.0, 1.0, n)
X, Y = np.meshgrid(x, y)                          # 2-D coordinate arrays
T = np.sin(np.pi * X) * np.sinh(np.pi * Y) / np.sinh(np.pi)   # Laplace soln

fig, ax = new_figure()
pcm = ax.pcolormesh(X, Y, T, shading="auto", cmap="magma")
cs = ax.contour(X, Y, T, levels=8, colors="white", linewidths=0.6)
ax.clabel(cs, inline=True, fontsize=8)
fig.colorbar(pcm, ax=ax, label="temperature")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_aspect("equal")
ax.set_title("Steady temperature field")
fig.savefig("field.png")

if __name__ == "__main__":
    print("wrote field.png")

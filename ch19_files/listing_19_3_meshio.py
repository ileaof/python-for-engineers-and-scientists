"""Listing 19.3 -- Reading and writing a mesh with a solution field via meshio;
writing .vtu opens the result directly in ParaView.

Requires: meshio, numpy.
Run:  python listing_19_3_meshio.py

Python for Engineers and Scientists, Chapter 19.
"""

from __future__ import annotations

import meshio
import numpy as np

if __name__ == "__main__":
    points = np.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])
    cells = [("triangle", np.array([[0, 1, 2], [0, 2, 3]]))]
    point_data = {"temperature": np.array([300.0, 320.0, 350.0, 310.0])}

    mesh = meshio.Mesh(points, cells, point_data=point_data)
    mesh.write("result.vtu")

    m = meshio.read("result.vtu")
    print(m.points.shape, m.point_data["temperature"].mean())

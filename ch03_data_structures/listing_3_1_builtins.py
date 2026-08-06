"""Listing 3.1 -- Matching the built-in container to the task.

Python for Engineers and Scientists, Chapter 3.
Run:  python listing_3_1_builtins.py
"""

coord = (0.5, 0.25, 0.0)                 # tuple: a fixed 3-D point

fluids = {                               # dict: O(1) lookup by name
    "air":   dict(rho=1.184, mu=1.849e-5),
    "water": dict(rho=997.0, mu=8.90e-4),
}

boundary_nodes = {0, 1, 2, 61, 62, 63}   # set: O(1) membership test
is_boundary = 62 in boundary_nodes       # True, without scanning

residuals = []                           # list: grows each iteration
for it in range(5):
    residuals.append(1.0 / (it + 1))


if __name__ == "__main__":
    print("coord         =", coord)
    print("rho(air)      =", fluids["air"]["rho"])
    print("62 boundary?  =", is_boundary)
    print("residuals     =", residuals)

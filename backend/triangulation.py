import numpy as np

def triangulate(stations, directions):
    """
    stations: Nx3 array of station positions (ECEF)
    directions: Nx3 array of unit direction vectors
    """

    A = np.zeros((3,3))
    b = np.zeros(3)

    for p, d in zip(stations, directions):

        d = d / np.linalg.norm(d)

        I = np.identity(3)

        A += I - np.outer(d, d)
        b += (I - np.outer(d, d)) @ p

    point = np.linalg.solve(A, b)

    return point
# f(u, v, t) = u + t \ (v - u)
# Using fuse multiply add
# f(u, v, t) = (1 - t)u + tv


import math
from math_lib import Vector, Matrix

def lerp(u, v, t: float):
    """
    Computes the linear interpolation between u and v
    u and v can be scalar (int/floats), vectors or matrices.
    """
    t = float(t)
    #Case 1: Scalars
    if isinstance(u, (int, float)) and isinstance(v, (int, float)):
        return math.fma(t, float(v), (1.0 - t) * float(u))
    #Case 2: Vectors
    if isinstance(u, Vector) and isinstance(v, Vector):
        if u.size != v.size:
            raise ValueError("Vector must be the same size for lerp.")
        new_data = [
            math.fma(t, v.data[i], (1.0 - t) * u.data[i])
            for i in range(u.size)
        ]
        return Vector(new_data)
    #Case 3: Matrices
    if isinstance(u, Matrix) and isinstance(v, Matrix):
        if u.shape != v.shape:
            raise ValueError("Matrices must have the same shape for lerp.")
        new_data = []
        for row in range(u.rows):
            new_row = [
                math.fma(t, v.data[row][col], (1.0 -t) * u.data[row][col])
                for col in range(u.cols)
            ]
            new_data.append(new_row)
        return Matrix(new_data)
    raise TypeError("Unsupported types for lerp or types do not match.")
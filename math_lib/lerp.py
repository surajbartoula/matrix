# f(u, v, t) = u + t \ (v - u)
# Using fuse multiply add
# f(u, v, t) = (1 - t)u + tv


import math
import math_lib


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
    if isinstance(u, math_lib.vector) and isinstance(v, math_lib.vector):
        if u.size != v.size:
            raise ValueError("Vector must be the same size for lerp.")
        new_data = [
            math.fma(t, v.data[i], (1.0 - t) * u.data[i])
            for i in range(u.size)
        ]
        return math_lib.vector(new_data)
    #Case 3: Matrices
    if isinstance(u, math_lib.matrix) and isinstance(v, math_lib.matrix):
        if u.shape != v.shape:
            raise ValueError("Matrices must have the same shape for lerp.")
        new_data = []
        for row in range(u.rows):
            new_row = [
                math.fma(t, v.data[row][col], (1.0 -t) * u.data[row][col])
                for col in range(u.cols)
            ]
            new_data.append(new_row)
        return math_lib.matrix(new_data)
    raise TypeError("Unsupported types for lerp or types do not match.")
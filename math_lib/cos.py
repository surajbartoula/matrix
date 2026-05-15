import math_lib


def angle_cos(u: math_lib.vector, v: math_lib.vector) -> float:
    """
    Computes the cosine of the angle between vectors u and v.
    Formula: (u.v) / (||u|| * ||v||)
    """
    if u.size != v.size:
        raise ValueError("Vectors must be the same size.")
    # Calculate the dot product
    dot_prod = u.dot(v)
    # Calculate the Euclidean norms
    norm_u = u.norm()
    norm_v = v.norm()
    # If a vector is zero, the angle is undefined
    if norm_u == 0.0 or norm_v == 0.0:
        return 0.0
    return dot_prod / (norm_u * norm_v)

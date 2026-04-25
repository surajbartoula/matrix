import math
import math_lib

def linear_combination(vectors, coefs):
    """
    Computes the linear combination of a list of vectors.
    vectors: list of Vectors objects
    coefs: list of scalars (floats)
    """
    if not vectors or not coefs or len(vectors) != len(coefs):
        return None
    dim = vectors[0].size
    res_data = [0.0] * dim
    for v, lamda_i in zip(vectors, coefs):
        if v.size != dim:
            raise ValueError("All vectors must have the same dimension.")
        for i in range(dim):
            # Using math.fma(a, b, c) -> (a * b) + c
            res_data[i] = math.fma(v.data[i], float(lamda_i), res_data[i])
    return math_lib.Vector(res_data)
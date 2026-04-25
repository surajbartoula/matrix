import math_lib
import math


def cross_product(u: math_lib.vector, v: math_lib.vector) -> math_lib.vector:
    """
    Computes the cross product of two 3D vectors.
    """
    if u.size != 3 or v.size != 3:
        raise ValueError("Cross product is only defined for 3D vectors.")
    #Converting into math.fma(a*b - c*d)
    x = math.fma(u.data[1], v.data[2], -(u.data[2] * v.data[1]))
    y = math.fma(u.data[2], v.data[0], -(u.data[0] * v.data[2]))
    z = math.fma(u.data[0], v.data[1], -(u.data[1] * v.data[0]))
    return math_lib.vector([x, y, z])
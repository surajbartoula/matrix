import math
from math_lib import Matrix


def projection(fov: float, ratio: float, near: float, far: float) -> 'Matrix':
    # Convert fov from degree to radians
    fov_rad = fov * math.pi / 180.0
    # a is the focal length
    a = 1.0 / math.tan(fov_rad / 2.0)
    # rows on column major as per the requirement
    row0 = [a / ratio, 0.0, 0.0, 0.0]
    row1 = [0.0, a, 0.0, 0.0]
    row2 = [0.0, 0.0, far / (far - near), 1.0]
    row3 = [0.0, 0.0, -(far * near) / (far - near), 0.0]
    return Matrix([row0, row1, row2, row3])

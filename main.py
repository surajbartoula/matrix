from math_lib import Matrix, Vector, cross_product, angle_cos, linear_combination, lerp


def test_cross_product():
    print("--- Exercise 06: Cross Product ---")
    u1, v1 = Vector([0., 0., 1.]), Vector([1., 0., 0.])
    print(f"u1 X v1 = {cross_product(u1, v1)}")

    u2, v2 = Vector([1., 2., 3.]), Vector([4., 5., 6.])
    print(f"u2 X v2 = {cross_product(u2, v2)}")

    u3, v3 = Vector([4., 2., -3.]), Vector([-2., -5., 16.])
    print(f"u3 X v3 = {cross_product(u3, v3)}")

def test_trace():
    print("--- Exercise 08: Trace ---")
    u1 = Matrix([
        [1., 0.],
        [0., 1.]
    ])
    print(f"Identity 2x2: {u1.trace()}")

    u2 = Matrix([
        [2., 4., -2.],
        [-5., 3., 3.],
        [0., 7., 4.]
    ])
    print(f"Example 2: {u2.trace()}")

    u3 = Matrix([
        [-2, 1., 0.],
        [-8., -23., 6.],
        [4., 4., 4.]
    ])
    print(f"Example 3: {u3.trace()}")

def test_transpose():
    print("--- Exercise 09: Transpose ---")
    m1 = Matrix([
        [1., 3.],
        [2., 4.]
    ])
    print("Original 2x2:")
    print(m1)
    print("Transposed:")
    print(m1.transpose())

    m2 = Matrix([
        [1., 4.],
        [2., 5.],
        [3., 6.]
    ])
    print("\nOriginal 2x3:")
    print(m2)
    t2 = m2.transpose()
    print("Transpose (Should be 3x2):")
    print(t2)
    print(f"New shape: {t2.shape}")

def test_rref():
    print("--- Exercise 10: RREF (Row-Major) ---")
    m1 = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.],
    ])
    print("Identity 3x3:")
    print(m1.row_echelon(), end="\n\n")
    m2 = Matrix([
        [1., 2.],
        [3., 4.]
    ])
    print(m2.row_echelon(), end="\n\n")
    m3 = Matrix([
        [1., 2.],
        [2., 4.]
    ])
    print(m3.row_echelon(), end="\n\n")
    m4 = Matrix([
        [8.0, 5.0, -2.0, 4.0, 28.0],
        [4.0, 2.5, 20.0, 4.0, -4.0],
        [8.0, 5.0, 1.0, 4.0, 17.0]
    ])
    print(m4.row_echelon())

def test_determinant():
    print("--- Exercise 11: Determinant ---")
    u1 = Matrix([
        [1., -1.],
        [-1., 1.]
    ])
    print(u1.determinant(), end="\n\n")
    u2 = Matrix([
        [2.0, 0., 0.],
        [0., 2., 0.],
        [0., 0., 2.],
    ])
    print(u2.determinant(), end="\n\n")
    u3 = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.],
    ])
    print(u3.determinant(), end="\n\n")
    u4 = Matrix([
        [8., 5., -2., 4.],
        [4., 2.5, 20., 4.],
        [8., 5., 1., 4.],
        [28., -4., 17., 1.],
    ])
    print(u4.determinant(), end="\n\n")

def test_inverse():
    print("--- Exercise 12: Inverse ---")
    u1 = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.],
    ])
    print(u1.inverse(), end="\n\n")
    print
    u2 = Matrix([
        [2.0, 0.0, 0.0],
        [0., 2., 0.],
        [0., 0., 2.],
    ])
    print(u2.inverse(), end="\n\n")
    u3 = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.],
    ])
    print(u3.inverse())


# def main():
#     print("---Vector Addition---")
#     u = Vector([2., 3.])
#     v = Vector([5., 7.])
#     u.add(v)
#     print(u)

#     print("\n---Matrix Scaling---")
#     u_mat = Matrix([
#         [1., 3.],
#         [2., 4.]
#     ])
#     u_mat.scl(2.)
#     print(u_mat)


if __name__ == "__main__":
    test_cross_product()
    test_trace()
    test_transpose()
    test_rref()
    test_determinant()
    test_inverse()

import math_lib


def test_cross_product():
    print("--- Exercise 06: Cross Product ---")
    u1, v1 = math_lib.vector([0., 0., 1.]), math_lib.vector([1., 0., 0.])
    print(f"u1 X v1 = {math_lib.cross_product(u1, v1)}")

    u2, v2 = math_lib.vector([1., 2., 3.]), math_lib.vector([4., 5., 6.])
    print(f"u2 X v2 = {math_lib.cross_product(u2, v2)}")

    u3, v3 = math_lib.vector([4., 2., -3.]), math_lib.vector([-2., -5., 16.])
    print(f"u3 X v3 = {math_lib.cross_product(u3, v3)}")

def test_ex08_trace():
    print("--- Exercise 08: Trace ---")
    u1 = math_lib.matrix([
        [1., 0.],
        [0., 1.]
    ])
    print(f"Identity 2x2: {u1.trace()}")

    u2 = math_lib.matrix([
        [2., 4., -2.],
        [-5., 3., 3.],
        [0., 7., 4.]
    ])
    print(f"Example 2: {u2.trace()}")

    u3 = math_lib.matrix([
        [-2, 1., 0.],
        [-8., -23., 6.],
        [4., 4., 4.]
    ])
    print(f"Example 3: {u3.trace()}")


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
    test_ex08_trace()

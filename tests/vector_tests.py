from math_lib import Vector, cross_product, angle_cos


def vector_operations():
    print("--- Vector Addition ---")
    u = Vector([2., 3.])
    v = Vector([5., 7.])
    u.add(v)
    print(u)
    print("--- Vector Substraction ---")
    u = Vector([2., 3.])
    v = Vector([5., 7.])
    u.sub(v)
    print(u)
    print("--- Vector scaling ---")
    u = Vector([2., 3.])
    u.scl(2)
    print(u)


def test_dot_product():
    print("--- Dot Product ---")
    u = Vector([0., 0.])
    v = Vector([1., 1.])
    print(u.dot(v))
    u = Vector([1., 1.])
    v = Vector([1., 1.])
    print(u.dot(v))
    u = Vector([-1., 6.])
    v = Vector([3., 2.])
    print(u.dot(v))

def test_norm():
    print("--- Norm ---")
    u = Vector([0., 0., 0.])
    print(u.norm_1(), u.norm(), u.norm_inf())
    u = Vector([1., 2., 3.])
    print(u.norm_1(), f"{u.norm():.9f}", u.norm_inf())
    u = Vector([-1., -2.])
    print(u.norm_1(), f"{u.norm():.9f}", u.norm_inf())

def test_cosine():
    print("--- Cosine ---")
    u = Vector([1., 0.])
    v = Vector([1., 0.])
    print(angle_cos(u, v))
    u = Vector([1., 0.])
    v = Vector([0., 1.])
    print(angle_cos(u, v))
    u = Vector([-1., 1.])
    v = Vector([1., -1.])
    print(f"{angle_cos(u, v):.1f}")
    u = Vector([2., 1.])
    v = Vector([4., 2.])
    print(f"{angle_cos(u, v):.1f}")
    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print(f"{angle_cos(u, v):.9f}")

def test_cross_product():
    print("--- Exercise 06: Cross Product ---")
    u1, v1 = Vector([0., 0., 1.]), Vector([1., 0., 0.])
    print(f"{cross_product(u1, v1)}", end="\n\n")

    u2, v2 = Vector([1., 2., 3.]), Vector([4., 5., 6.])
    print(f"{cross_product(u2, v2)}", end="\n\n")

    u3, v3 = Vector([4., 2., -3.]), Vector([-2., -5., 16.])
    print(f"{cross_product(u3, v3)}")

def run_vector_test():
    vector_operations()
    test_dot_product()
    test_norm()
    test_cosine()
    test_cross_product()


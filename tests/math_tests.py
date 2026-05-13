from math_lib import Matrix, Vector, linear_combination, lerp


def test_linear_combination():
    print("--- Linear Combination ---")
    e1 = Vector([1., 0., 0.])
    e2 = Vector([0., 1., 0.])
    e3 = Vector([0., 0., 1.])
    v1 = Vector([1., 2., 3.])
    v2 = Vector([0., 10., -100.])
    print(linear_combination([e1, e2, e3], [10., -2., 0.5]))
    print(linear_combination([v1, v2], [10., -2.]))

def test_lerp():
    print("--- Lerp ---")
    print(f"{lerp(0., 1., 0.):.1f}")
    print(f"{lerp(0., 1., 1.):.1f}")
    print(f"{lerp(0., 1., 0.5):.1f}")
    print(f"{lerp(21., 42., 0.3):.1f}")
    res = lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3)
    print(f"{res:.1f}")
    print(lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20., 10.], [30., 40.]]), 0.5))

def run_math_test():
    test_linear_combination()
    test_lerp()
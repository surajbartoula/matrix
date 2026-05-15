from tests.math_tests import run_math_test
from tests.vector_tests import run_vector_test
from tests.matrix_tests import run_matrix_test


def run_all():
    run_vector_test()
    run_matrix_test()
    run_math_test()


if __name__ == "__main__":
    run_all()

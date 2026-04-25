import math
import math_lib


class Matrix:
    def __init__(self, data):
        # data is a list of lists: [[row1_col1, row1_col2], [row2_col1, row2_col2]]
        self.data = [[float(item) for item in row] for row in data]
        self.rows = len(self.data)
        self.cols = len(self.data[0]) if self.data else 0
        self.shape = (self.rows, self.cols)

    def add(self, m):
        if self.shape != m.shape:
            raise ValueError("Matrices must have the same shape.")
        for r in range(self.rows):
            for c in range(self.cols):
                self.data[r][c] += m.data[r][c]

    def sub(self, m):
        if self.shape != m.shape:
            raise ValueError("Matrices must have the same shape.")
        for r in range(self.rows):
            for c in range(self.cols):
                self.data[r][c] -= m.data[r][c]

    def mul_vec(self, v: math_lib.vector) -> math_lib.vector:
        """
        Matrix-Vector Multiplication: O(rows * cols)
        """
        if self.cols != v.size:
            raise ValueError("Matrix columns must match Vector Size.")
        res_data = [0.0] * self.rows
        for r in range(self.rows):
            for c in range(self.cols):
                # Row-major access: [row][col]
                res_data[r] = math.fma(self.data[r][c], v.data[c], res_data[r])
        return math_lib.vector(res_data)

    def mul_mat(self, m: 'Matrix') -> 'Matrix':
        """
        Matrix-Matrix Multiplication: O(n^3)
        """
        if self.cols != m.rows:
            raise ValueError("Matrix A columns must match Matrix B rows.")
        # Initialize new_data in column-major: list of columns
        new_data = [[0.0 for _ in range(m.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(m.cols):
                dot_sum = 0.0
                for i in range(self.cols):  # Inner dimensions
                    dot_sum = math.fma(self.data[r][i], m.data[i][c], dot_sum)
                new_data[r][c] = dot_sum
        return Matrix(new_data)

    def trace(self) -> float:
        """
        Computes the trace of the matrix (sum of diagonal elements.)
        Complexity: O(n) where n is the number of rows/cols.
        """
        if not self.is_square():
            raise ValueError("Trace is only defined for square matrices.")
        res = 0.0
        for i in range(self.rows):
            res += self.data[i][i]
        return res

    def scl(self, a):
        a_float = float(a)
        for r in range(self.rows):
            for c in range(self.cols):
                self.data[r][c] *= a_float

    def is_square(self) -> bool:
        return self.rows == self.cols

    def __str__(self):
        res = ""
        for row in self.data:
            res += f"[{', '.join(map(str, row))}]\n"
        return res.strip()
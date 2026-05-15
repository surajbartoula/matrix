import math
from math_lib import Vector


class Matrix:
    def __init__(self, data: list[list[float]]):
        if not data or not any(data):
            self.data = [[]]
            self.rows = 0
            self.cols = 0
        else:
            # data is a list of lists:
            # [[row1_col1, row1_col2], [row2_col1, row2_col2]]
            self.rows = len(data)
            self.cols = len(data[0])
            for i in range(self.rows):
                if len(data[i]) != self.cols:
                    msg = f"Row {i}: expected {self.cols} cols"
                    raise ValueError(msg)
            self.data = [[float(item) for item in row] for row in data]
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

    def mul_vec(self, v: Vector) -> Vector:
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
        return Vector(res_data)

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
        return self.__class__(new_data)

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

    def transpose(self) -> 'Matrix':
        """
        Returns the transpose of the Matrix.
        Rows become columns and columns become rows.
        Complexity: O(nm)
        """
        # Original shape: (rows, cols) and new shape: (cols, rows)
        new_data = [
            [self.data[r][c] for r in range(self.rows)
                for c in range(self.cols)]
        ]
        return self.__class__(new_data)

    def row_echelon(self) -> 'Matrix':
        """
        Computes the Reduced Row Echelon Form(RREF): O(n^3)
        """
        matrix = [row[:] for row in self.data]  # Deep copy of matrix
        num_rows = len(matrix)
        num_cols = len(matrix[0]) if num_rows > 0 else 0
        pivot_row = 0
        for pivot_col in range(num_cols):
            if pivot_row >= num_rows:
                break
            # Step 1: Find the best row for this pivot (Partial Pivoting)
            sel_row = pivot_row
            # Finiding non-zero pivot
            for r in range(pivot_row, num_rows):
                if abs(matrix[r][pivot_col]) > abs(matrix[sel_row][pivot_col]):
                    sel_row = r
            # If the best candidate is effectively zero, skip this column
            if abs(matrix[sel_row][pivot_col]) < 1e-9:
                continue
            # Swap current row with sel_row
            matrix[pivot_row], matrix[sel_row] = (
                matrix[sel_row], matrix[pivot_row]
                )
            # Step 2: Normalize pivot row(Leading entry becomes 1)
            pivot_val = matrix[pivot_row][pivot_col]
            matrix[pivot_row] = [x / pivot_val for x in matrix[pivot_row]]
            # Step 3: Eliminate all other entries in this column
            for r in range(num_rows):
                if r != pivot_row:
                    factor = matrix[r][pivot_col]
                    for c in range(pivot_col, num_cols):
                        # matrix[r][c] -= factor * matrix[pivot_row][c]
                        matrix[r][c] = math.fma(
                            -factor, matrix[pivot_row][c], matrix[r][c]
                            )
            pivot_row += 1
        return self.__class__(matrix)

    def determinant(self) -> float:
        if not self.is_square():
            msg = "Determinant can only be calculated for square matrices."
            raise ValueError(msg)
        if self.rows == 0:
            return 1.0
        if self.rows == 1:
            return float(self.data[0][0])
        if self.rows == 2:
            # ad - bc
            # return float(self.data[0][0] * self.data[1][1]
            # - self.data[0][1] * self.data[1][0])
            return math.fma(
                self.data[0][0], self.data[1][1],
                -(self.data[0][1] * self.data[1][0])
                )
        # For 3x3 & 4x4, we use the row reduction method
        matrix = [row[:] for row in self.data]
        n = self.rows
        det = 1.0
        for i in range(n):
            # 1. Pivot Selection (Partial Pivoting)
            pivot = i
            for j in range(i + 1, n):
                if abs(matrix[j][i]) > abs(matrix[pivot][i]):
                    pivot = j
            # If we swap rows, the determinant flips sign
            if pivot != i:
                matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
                det *= -1
            # If the diagonal element is 0, the determinant is 0
            if abs(matrix[i][i]) < 1e-9:
                return 0.0
            # 2. Elimination (No need to normalize the row to 1.0)
            # Just zero out everything below the diagonal
            for j in range(i + 1, n):
                factor = matrix[j][i] / matrix[i][i]
                for k in range(i + 1, n):
                    # matrix[j][k] -= factor * matrix[i][k]
                    matrix[j][k] = math.fma(
                        -factor, matrix[i][k], matrix[j][k]
                        )
            # 3. Multiply the determinant by the diagonal element.
            det *= matrix[i][i]
        return det

    def inverse(self) -> 'Matrix':
        if not self.is_square():
            raise ValueError("Only square matrices have a inverse.")
        n = self.rows
        # Create the augmented matrix [A | I]
        # Space complexity: O(n^2)
        aug = []
        for i in range(n):
            identity_row = [1.0 if j == i else 0.0 for j in range(n)]
            # Row-major: self.data[i] is the row
            aug.append([float(x) for x in self.data[i] + identity_row])
        # Gauss-Jordan Elimination
        for i in range(n):
            # 1. Partial Pivoting (for numeric stability)
            pivot = i
            for j in range(i + 1, n):
                if abs(aug[j][i]) > abs(aug[pivot][i]):
                    pivot = j
            aug[i], aug[pivot] = aug[pivot], aug[i]
            # 2. Check for singularity
            if abs(aug[i][i]) < 1e-10:
                raise ValueError("Matrix is singular and cannot be inverted.")
            # 3. Normalize pivot row to 1
            pivot_val = aug[i][i]
            for j in range(i, 2 * n):
                aug[i][j] /= pivot_val
            # 4. Eliminate other rows (Above and Below)
            for j in range(n):
                if i != j:
                    factor = aug[j][i]
                    # Applying fused multiply-add: aug[j][k]
                    # = (-factor * aug[i][k]) + aug[j][k]
                    for k in range(i, 2 * n):
                        aug[j][k] = math.fma(-factor, aug[i][k], aug[j][k])
        # Extract the right side [I | A^-1]
        inv_data = [row[n:] for row in aug]
        return self.__class__(inv_data)

    def rank(self) -> int:
        rref_matrix = self.row_echelon()
        rank_count = 0
        # Count how many rows are not all zeros
        for row in rref_matrix.data:
            # Check if any element in the row is significantly
            # different from zero
            if any(abs(elem) > 1e-9 for elem in row):
                rank_count += 1
        return rank_count

    def scl(self, a):
        a_float = float(a)
        for r in range(self.rows):
            for c in range(self.cols):
                self.data[r][c] *= a_float

    def is_square(self) -> bool:
        return self.rows == self.cols

    def __str__(self):
        rows = []
        for row in self.data:
            formatted_row = [f"{x}" for x in row]
            rows.append("[" + ", ".join(formatted_row) + "]")
        return "\n".join(rows)

    def __format__(self, format_spec):
        return "\n".join(
            "[" + ", ".join(format(x, format_spec) for x in row) + "]"
            for row in self.data
        )

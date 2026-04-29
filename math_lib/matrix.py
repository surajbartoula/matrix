import math
import math_lib


class Matrix:
    def __init__(self, data: list[list[float]]):
        if not data or not any(data):
            self.data = [[]]
            self.rows = 0
            self.cols = 0
        else:
            # data is a list of lists: [[row1_col1, row1_col2], [row2_col1, row2_col2]]
            self.rows = len(data)
            self.cols = len(data[0])
            for i in range(self.rows):
                if len(data[i]) != self.cols:
                    raise ValueError(f"Row {i} has {len(data[i])} columns, expected {self.cols}")
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
            [self.data[c][r] for c in range(self.cols)
                            for r in range(self.rows)]
        ]
        return self.__class__(new_data)

    def row_echelon(self) -> 'Matrix':
        """
        Computes the Reduced Row Echelon Form(RREF): O(n^3)
        """
        rows_list = []
        for r in range(self.rows):
            rows_list.append([self.data[c][r] for c in range(self.cols)])
        pivot_row = 0
        for pivot_col in range(self.cols):
            if pivot_row >= self.rows:
                break
            # Step 1: Find the best row for this pivot (Partial Pivoting)
            sel_row = pivot_row
            while sel_row < self.rows and abs(rows_list[sel_row][pivot_col] < 1e-9):
                sel_row += 1
            if sel_row == self.rows: # No pivot in this column
                continue
            # Swap current row with sel_row
            rows_list[pivot_row], rows_list[sel_row] = rows_list[sel_row], rows_list[pivot_row]
            # Step 2: Normalize pivot row so pivot elements becomes 1
            pivot_val = rows_list[pivot_row][pivot_col]
            rows_list[pivot_row] = [x / pivot_val for x in rows_list[pivot_row]]
            # Step 3: Eliminate all other entries in this column(above and below)
            for r in range(self.rows):
                if r != pivot_row:
                    factor = rows_list[r][pivot_col]
                    rows_list[r] = [
                        rows_list[r][i] - factor * rows_list[pivot_row][i]
                        for i in range(self.cols)
                    ]
            pivot_row += 1
        new_col_major = []
        for c in range(self.cols):
            new_col = [rows_list[r][c] for r in range(self.rows)]
            new_col_major.append(new_col)
        return self.__class__(new_col_major)

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
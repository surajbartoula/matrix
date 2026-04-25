import math

class Vector:
    def __init__(self, data):
        # Data is a list of floats (K)
        self.data = [float(x) for x in data]
        self.size = len(self.data)

    def add(self, v):
        if self.size != v.size:
            raise ValueError("Vector must be the same size for addition.")
        for i in range(self.size):
            self.data[i] += v.data[i]

    def sub(self, v):
        if self.size != v.size:
            raise ValueError("Vector must be the same size for substraction.")
        for i in range(self.size):
            self.data[i] -= v.data[i]

    def scl(self, a):
        for i in range(self.size):
            self.data[i] *= float(a)

    def dot(self, v) -> float:
        """
        Computes the dot product of this vector and another vector v.
        Returns a scalar (float).
        Returns a scalar (float).
        """
        if self.size != v.size:
            raise ValueError("Vectors must be of the same dimension for a dot product.")
        res = 0.0
        for i in range(self.size):
            res = math.fma(self.data[i], v.data[i], res)
        return res

    def norm_1(self) -> float:
        """
        Manhattan or Taxicab Norm
        """
        res = 0.0
        for x in self.data:
            res += abs(x)
        return res

    def norm(self) -> float:
        """
        Euclidean Norm
        """
        if not self.data:
            return 0.0
        sum_sq = 0.0
        for x in self.data:
            # x^2 + sum_sq using fused multiply-add
            sum_sq = math.fma(x, x, sum_sq)
        # Square root using pow(x, 0.5)
        return math.pow(sum_sq, 0.5)

    def norm_inf(self) -> float:
        """
        Supremum Norm
        """
        if not self.data:
            return 0.0
        res = 0.0
        for x in self.data:
            #max(current_max, absolute_value)
            res = max(res, abs(x))
        return res

    def __str__(self):
        # Formatting to match the column-style output
        return "[" + " ".join([f"{x}" for x in self.data]) + "]"

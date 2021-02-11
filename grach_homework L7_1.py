m1 = [[1, 1] if k == l else [0, 0] for k in range(1) for l in range(2)]
m2 = [[1, 1] if k != l else [0, 0] for k in range(1) for l in range(2)]
print(f"\n\nInput Matrix1 & Matrix2:\n{m1}\n{m2}")
print(f"\nMatrix size: {len(m1)}x{len(m1[0])}\n")


class Matrix:
    def __init__(self, matrix):
        self.md0, self.md1 = len(matrix), len(matrix[0])
        self.matrix = matrix

    # def __del__(self):
    #    print(f"\n*** Warning: computation completed & object deleted. ***")

    def __str__(self):
        st = ""
        for k in range(self.md0):
            for j in range(self.md1):
                st += str(self.matrix[k][j]) + "\t"
            st += "\n"
        return f'{st}'

    def __add__(self, other):
        try:
            z = [[0, 0] for _ in range(self.md0)]
            for k in range(self.md0):
                for j in range(self.md1):
                    z[k][j] = self.matrix[k][j] + other.matrix[k][j]
                    # print(f'z={z[k][j]}, {k}, {j}')
            return z
        except:
            print(f"\n*** Error in matrix dimension ***")


matrix1 = Matrix(m1)
matrix2 = Matrix(m2)
print(f'matrix1:\n{matrix1}')
print(f'matrix2:\n{matrix2}')

w = matrix1 + matrix2
print(f'matrix1 + matrix2:')
st = ""
for k in range(len(w)):
    for j in range(len(w[0])):
        st += str(w[k][j]) + "\t"
    st += "\n"
print(f'{st}')
matrix_a = [[3, 6], [4, 5]]
matrix_b = [[5, 8], [6, 7]]

result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]

print(result)

# Scalar-Matrix Product

matrix_c = [[3, 6], [4, 5]]
alpha = 4

result = [[alpha * element for element in t]for t in matrix_c]

print(result)

# Matrix Transpose

matrix_d = [[1, 2, 3], [4, 5, 6]]

result = [[element for element in t] for t in zip(*matrix_d)]

print(result)

# Matrix Product

matrix_e = [[1, 1, 2], [2, 1, 1]]
matrix_f = [[1, 1], [2, 1], [1, 3]]

result = [[sum(a * b for a, b in zip(row_a, column_b))
           for column_b in zip(*matrix_f)] for row_a in matrix_e]

print(result)

# 두 개 이상의 argument가 존재할 때


def vector_addition(*args):
    return [t for t in zip(*args)]


print(vector_addition([1, 2], [2, 3], [3, 4]))

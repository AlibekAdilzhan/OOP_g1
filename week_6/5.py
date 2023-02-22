def get_matrix_sum(matrix, n):
    s = 0
    for i in range(n):
        for j in range(n):
            s += matrix[i][j]
    return s


matrix = [
    [1, 2],
    [2, 5]
]
print(get_matrix_sum(matrix, 2))



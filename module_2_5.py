def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        one = []
        for j in range(m):
            one.append(value)
        matrix.append(one)
    return matrix
result = get_matrix(4, 3, 8)
print(result)
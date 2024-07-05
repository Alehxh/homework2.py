def get_matrix(n, m, value):
    if n <= 0 or m <= 0:
        return []

    matrix = []
    for _ in range(n):
        row = [value] * m
        matrix.append(row)
    return matrix
result1 = get_matrix(2, 2, 10)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result3)   
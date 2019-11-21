from functools import reduce

with open("input.txt", "r") as fin:
    n, m = list(map(int, fin.readline().strip().split()))
    matrix = [list(map(float, fin.readline().strip().split())) for i in range(n)]

result = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(i, n):
        xm = sum(matrix[i]) / m
        ym = sum(matrix[j]) / m
        xd = reduce(lambda a, x: a + (x - xm) ** 2, matrix[i], 0) / m
        yd = reduce(lambda a, y: a + (y - ym) ** 2, matrix[j], 0) / m
        cov = sum(map(lambda x, y: (x - xm) * (y - ym), matrix[i], matrix[j])) / m
        result[i][j] = result[j][i] = cov / ((xd * yd) ** 0.5)

with open("output.txt", "w") as fout:
    for i in range(n):
        print(*result[i], file=fout)

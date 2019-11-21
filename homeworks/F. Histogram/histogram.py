import math

with open("input.txt", "r") as fin:
    n = int(fin.readline().strip())
    a = list(map(float, fin.readline().strip().split()))

k = 1 + int(math.log2(n))
result = [0] * k
minimum = min(a)
size = (max(a) - minimum) / k
for elem in a:
    index = k - 1
    e = elem - minimum
    if size != 0 and e != size * k:
        index = e // size
    result[int(index)] += 1

with open("output.txt", "w") as fout:
    print(*result, file=fout)

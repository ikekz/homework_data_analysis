with open("input.txt", "r") as fin:
    n, k = list(map(int, fin.readline().strip().split()))
    sample = list(map(float, fin.readline().strip().split()))

e = sum(sample) / n
m = sum(map(lambda x: ((x - e) ** k), sample)) / n

with open("output.txt", "w") as fout:
    print(m, file=fout)

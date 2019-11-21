from functools import reduce

with open("input.txt", "r") as fin:
    n = int(fin.readline().strip())
    sample = list(map(float, fin.readline().strip().split()))

with open("output.txt", "w") as fout:
    print(n / sum(map(lambda x: 1 / x, sample)), file=fout)

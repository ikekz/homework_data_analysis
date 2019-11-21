import math

with open("input.txt", "r") as fin:
    n = int(fin.readline().strip())
    sample = list(map(int, fin.readline().strip().split()))

dict = {}
for x in sorted(sample):
    dict[x] = dict.get(x, 0) + 1

s = sum(dict.values())

with open("output.txt", "w") as fout:
    print(*dict.keys(), file=fout)
    print(*dict.values(), file=fout)
    print(*map(lambda x: x / s, dict.values()), file=fout)

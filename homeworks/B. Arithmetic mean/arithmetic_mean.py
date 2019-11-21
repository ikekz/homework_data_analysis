with open("input.txt", "r") as fin:
    n = int(fin.readline().strip())
    sample = list(map(float, fin.readline().strip().split()))

with open("output.txt", "w") as fout:
    print(sum(sample) / n, file=fout)

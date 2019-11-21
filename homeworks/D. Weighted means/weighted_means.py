from functools import reduce

with open("input.txt", "r") as fin:
    n = int(fin.readline().strip())
    freq = {x:y for x, y in [list(map(float, fin.readline().strip().split())) for i in range(n)]}

wam = sum(map(lambda x, y: x * y, freq.keys(), freq.values())) / sum(freq.values())
whm = sum(freq.values()) / sum(map(lambda x, y: x / y, freq.values(), freq.keys()))
wgm = reduce(lambda x, y: x * y, map(lambda x, y: x ** y, freq.keys(), freq.values())) ** (1 / sum(freq.values()))

with open("output.txt", "w") as fout:
    print(f'{wam} {whm} {wgm}', file=fout)

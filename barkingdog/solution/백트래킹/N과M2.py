import itertools

n, m = map(int, input().split())

comb = itertools.combinations(range(1, n + 1), m)

for i in comb:
    print(*i, sep = ' ')
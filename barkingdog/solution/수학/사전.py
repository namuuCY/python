import itertools, sys

n, m, k = map(int, sys.stdin.readline().split())

azs = []

for i in range(n):
    azs.append('a')

for i in range(m):
    azs.append('z')

comb = list(itertools.permutations(azs, n + m))

print(comb)
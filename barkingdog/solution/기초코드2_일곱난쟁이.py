import sys
import itertools

x = []
for i in range(9):
    y = list(map(int, sys.stdin.readline().split()))
    x.extend(y)

comb = itertools.combinations(x, 7)

for z in comb:
    if sum(z) == 100:
        w = list(z)
        w.sort()
        print(*w , sep = '\n')
        break

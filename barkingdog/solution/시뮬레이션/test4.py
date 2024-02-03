import sys
from itertools import combinations

N = int(sys.stdin.readline())
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sum_stat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]

print(*sum_stat, sep = '\n')
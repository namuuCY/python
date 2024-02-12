import sys

n, k = map(int, input().split())
coins = list(map(int, sys.stdin.readlines().rstrip()))
coins.sort()
DP = {}
for i in range(n):
    DP[(0, coins[i])] = 0
for i in range(1, k+1):
    for j in range(n):
        DP
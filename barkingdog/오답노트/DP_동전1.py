import sys

n, k = map(int, input().split())
coins = list(map(int, sys.stdin.read().split()))
coins.sort()
DP = [0] * (k + 1)
DP[0] = 1
for i in range(n):
    for j in range(coins[i], k + 1):
        DP[j] += DP[j - coins[i]]

print(DP[k])
import sys

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(input())
    DP = [0] * (M + 1)
    DP[0] = 1
    for m in coins:
        for j in range(m, M + 1):
            DP[j] += DP[j - m]
    print(DP[M])
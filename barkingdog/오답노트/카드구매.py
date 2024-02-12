import sys
N = int(input())
card = [0] + list(map(int, sys.stdin.readline().split()))
DP = [0] * (N + 1)
for i in range(1, N + 1):
    DP[i] = max([DP[i - j] + card[j] for j in range(1, i + 1)])

print(DP[N])




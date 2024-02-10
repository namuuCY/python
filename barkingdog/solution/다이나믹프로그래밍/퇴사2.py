import sys
N = int(input())
T = [0]
P = [0]
DP = [0] * (N + 2)
for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

for i in range(N, 0, -1):
    if i + T[i] <= N + 1:
        DP[i] = max(DP[i], DP[i + 1] + P[i])
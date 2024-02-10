import sys
N  = int(input())
T = [0]
P = [0]
for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

DP = [0] * (N + 2)

for i in range(N, 0, -1):
    if i + T[i] <= N + 1:
        DP[i] = max(DP[i + T[i]] + P[i], DP[i + 1])
    else:
        DP[i] = DP[i + 1]
    
print(max(DP))

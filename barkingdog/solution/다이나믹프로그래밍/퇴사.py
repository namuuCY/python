import sys
N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)

for i in range(1, N + 1):
    T[i], P[i] = map(int, sys.stdin.readline().split())

DP = [0] * (N + 2) # i-1 번째 날에 상담 끝났을때 이익
for i in range(1, N + 1):
    DP[i] = max(DP[i], DP[i - 1])
    if i + T[i] - 1 > N :
        continue
    DP[i + T[i]] = max(DP[i] + P[i], DP[i + T[i]])

print(max(DP))
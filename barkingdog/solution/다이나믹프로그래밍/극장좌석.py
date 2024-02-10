import sys

N = int(input())
vnum = int(input())
vip = [False] * N
for _ in range(vnum):
    vip[int(input()) - 1] = True

DP = [[0 for _ in range(2)] for _ in range(N)]

if vip[0]:
    DP[0][0] = 1
    DP[0][1] = 0
else:
    DP[0][0] = 1
    DP[0][1] = 1

if N >= 2:
    for i in range(1, N):
        if vip[i]:
            DP[i][0] = DP[i - 1][0]
            DP[i][1] = 0
        else:
            DP[i][0] = DP[i - 1][0] + DP[i - 1][1]
            DP[i][1] = DP[i - 1][0]

print(max(DP[N - 1]))

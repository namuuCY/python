import sys


# 얻어걸린 풀이임.
# [i][0]을 i번째 사람이 앉는경우 [i][1]을 [i+1]번째 사람이 앉는경우로 설정
# 그러면 논리전개상으로는 맞는데 답이 틀렸음(값으로는 맞음.)
# 마지막사람은 자리를 바꿀수가 없으니까. 무조건 print(DP[N - 1][0])가 되어야함.

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

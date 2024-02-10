import sys

n = int(input())
wine = list(map(int, sys.stdin.read().split()))     # 계속틀리네 한줄에 걸쳐서 받는지 여러줄에 걸쳐서 받는지
DP = [[0 for _ in range(3)] for _ in range(n)]    #3번연속으로 마실수는 없음
DP[0][0] = 0
DP[0][1] = wine[0]
DP[0][2] = wine[0]

if n >= 2:
    for i in range(1, n):
        DP[i][0] = max(DP[i - 1][0], DP[i - 1][1], DP[i - 1][2])
        DP[i][1] = max(DP[i - 1][0] + wine[i], DP[i - 1][1])
        DP[i][2] = max(DP[i - 1][1] + wine[i], DP[i - 1][2])

print(max(DP[n - 1]))
import sys
input = sys.stdin.readline

N = int(input())
num = [0] + list(map(int, input().split()))
DP = [[0] * (N + 1) for _ in range(N + 1)]
ans = []
for i in range(1, N + 1):
    DP[i][i] = 1
    if num[i - 1] == num[i]:
        DP[i - 1][i] = 1

for gap in range(2, N):
    for i in range(1, N - gap + 1):
        if num[i] == num[i + gap] and DP[i + 1][i + gap - 1] == 1:
            DP[i][i + gap] = 1

for _ in range(int(input())):
    i, j  = map(int, input().split())
    ans.append(DP[i][j])

print(*ans, sep = '\n')

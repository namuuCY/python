import sys
N, M = map(int, input().split())        # N행 M열
board = [[0] * (M + 1) for _ in range(N + 1)]
ans = 0
for i in range(1, N + 1):
    s = sys.stdin.readline().strip()
    for j in range(1, M + 1):
        board[i][j] = int(s[j - 1])

DP = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if board[i][j] == 1:
            DP[i][j] = min(DP[i - 1][j], DP[i][j - 1], DP[i - 1][j - 1]) + 1
            ans = max(ans, DP[i][j])

print(ans * ans)

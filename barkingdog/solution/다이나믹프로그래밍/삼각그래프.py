import sys
k = 1

while True:
    N = int(input())
    if N == 0:
        break
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    DP = [[0] * 3 for _ in range(N)]
    DP[0][1] += board[0][1]
    DP[0][2] += board[0][2] + board[0][1]
    DP[1][0] = DP[0][1] + board[1][0]
    DP[1][1] = min(DP[0][1], DP[0][2], DP[1][0]) + board[1][1]
    DP[1][2] = min(DP[0][1], DP[0][2], DP[1][1]) + board[1][2]
    if N >= 3:
        for i in range(2, N):
            DP[i][0] = min(DP[i - 1][0], DP[i - 1][1]) + board[i][0]
            DP[i][1] = min(DP[i][0], DP[i - 1][0], DP[i - 1][1], DP[i - 1][2]) + board[i][1]
            DP[i][2] = min(DP[i - 1][1], DP[i - 1][2], DP[i][1]) + board[i][2]
    print(f'{k}. {DP[N - 1][1]}')
    k += 1
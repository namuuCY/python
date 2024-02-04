# 이거 답이 맞긴 할건데 시간초과임.

from itertools import combinations
import sys
# N이 세로선 개수 H가 점선개수
N, M, H = map(int, input().split())
board = [[0] * (N + 1) for _ in range(H + 1)]
coord = []
for _ in range(M):
    t1, t2 = map(int, sys.stdin.readline().split())
    board[t1][t2] = 1
for i in range(1, H + 1):
    for j in range(1, N):
        if board[i][j] == 1 or board[i][j + 1] == 1 or board[i][j - 1] == 1:
            continue
        coord.append((i, j))

def ck():
    for i in range(1, N + 1):
        now = i
        for j in range(1, H + 1):
            if board[j][now] == 1:
                now += 1
            elif board[j][now - 1] == 1:
                now -= 1
        if now != i:
            return False
    return True

def recur(n, idx):
    global ans
    if n >= ans:
        return
    if ck():
        ans = min(ans, n)
        return 
    if n == 3:
        return

    for c in range(idx, len(coord)):
        i, j = coord[c]
        if board[i][j - 1] == 1 or board[i][j + 1] == 1:
            continue
        board[i][j] = 1
        recur(n + 1, c + 1)
        board[i][j] = 0

ans = 4
recur(0, 0)
print(ans if ans != 4 else -1)

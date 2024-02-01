from collections import deque
import sys

# BFS와 백트래킹 이용.

def recur(n, tetro):
    global ans
    if n == 4:
        ans = max(ans, sum(board[i][j] for (i, j) in tetro))
        return
    for j in range(len(tetro)):
        x, y = tetro[j]
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in tetro and vis[nx][ny] == 0:
                tetro.append((nx, ny))          # (nx,ny) not in 이랑 vis가 핵심.
                recur(n + 1, tetro)
                tetro.pop()
        
N, M = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
vis = [[0] * M for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        tetro = []
        tetro.append((i, j))
        vis[i][j] = 1
        recur(1, tetro)

print(ans)
from collections import deque
import sys

input = sys.stdin.readline
n, m = list(map(int, input().split()))        # input은 string이라... 설명이필요한가

board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
Q = deque()
Q.append((0, 0))
dist = [[0] * m for _ in range(n)]
dist[0][0] = 1
vis = [[False] * m for _ in range(n)]

def met() -> None:
    while Q:
        x, y  = Q.popleft()
        for i in range(4):
            nx , ny = x + dx[i], y + dy[i]
            if nx < 0 or ny <0 or nx >= n or ny >= m:
                continue
            if board[nx][ny] == 1:
                vis[nx][ny] = True
            if board[nx][ny] == 0 and dist[nx][ny] == 0:
                dist[nx][nx] = dist[x][y] + 1
                Q.append((nx, ny))
met()
print(*vis, sep = '\n')






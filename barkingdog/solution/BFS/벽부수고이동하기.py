from collections import deque
import sys

input = sys.stdin.readline
n, m = list(map(int, input().split()))        # input은 string이라... 설명이필요한가

board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
Q = deque()
Q.append((0, 0))
dist = [[-1] * m for _ in range(n)]
dist[0][0] = 1
vis = [[False] * m for _ in range(n)]
ans = []
def met() -> int:
    while Q:
        x, y  = Q.popleft()
        for i in range(4):
            nx , ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if board[nx][ny] == 1:
                vis[nx][ny] = True
            if board[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                Q.append((nx, ny))
    return dist[n-1][m-1]

def bfs() -> int:
    while Q:
        x, y  = Q.popleft()
        for i in range(4):
            nx , ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if board[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                Q.append((nx, ny))
    return dist[n-1][m-1]

if met() != -1:
    ans.append(met())

else:
    for i in range(n):
        for j in range(m):
            if vis[i][j]:
                board[i][j] = 0
                Q.append((0, 0))
                dist = [[-1] * m for _ in range(n)]
                dist[0][0] = 1
                if bfs() != -1:
                    ans.append(bfs())
                board[i][j] = 1
if ans:
    print(min(ans))
else:
    print(-1)






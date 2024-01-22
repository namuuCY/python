from collections import deque
import sys


n = int(input().rstrip())
board = [sys.stdin.readline().rstrip() for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
Q = deque()
vis = [[False]*n for _ in range(n)]
bcount = 0
rcount = 0
gcount = 0
rgcount = 0

def bfs(x: int, y: int, color: str) -> int:
    Q.append((x, y))
    while Q:
        x,y = Q.popleft()
        for dir in range(4):
            nx, ny = x+ dx[dir], y+ dy[dir]
            if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and board[nx][ny] == color:
                vis[nx][ny] = True
                Q.append((nx, ny))
    return 1
def rgbfs(x: int, y: int) -> int:
    Q.append((x, y))
    while Q:
        x,y = Q.popleft()
        for dir in range(4):
            nx, ny = x+ dx[dir], y+ dy[dir]
            if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and board[nx][ny] != 'B':
                vis[nx][ny] = True
                Q.append((nx, ny))
    return 1
                
for i in range(n):
    for j in range(n):
        if board[i][j] == 'B' and not vis[i][j]:
            bcount += bfs(i, j, 'B')
        elif board[i][j] == 'G' and not vis[i][j]:
            gcount += bfs(i, j, 'G')
        elif board[i][j] == 'R' and not vis[i][j]:
            rcount += bfs(i, j, 'R')
print(bcount + gcount + rcount)
bcount = 0
vis = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 'B' and not vis[i][j]:
            bcount += bfs(i, j, 'B')
        elif (board[i][j] == 'G' or board[i][j] == 'R') and not vis[i][j]:
            rgcount += rgbfs(i, j)
print(bcount+rgcount)

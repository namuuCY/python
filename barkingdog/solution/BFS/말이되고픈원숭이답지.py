from collections import deque
import sys

k = int(input().rstrip())
w, h = map(int, input().split())        # h가 행의값
board = [ list(map(int, sys.stdin.readline().split())) for _ in range(h)]
dx = [1, 0, -1, 0, 2, 2, 1, 1, -1, -1, -2, -2]
dy = [0, 1, 0, -1, 1, -1, 2, -2, 2, -2, 1, -1]

Q = deque()
vis = [[[-1] * w for _ in range(h)] for _ in range(k + 1)]
for l in range(k + 1):
    vis[l][0][0] = 0
Q.append((0, 0, 0))

while Q:
    jump, x, y = Q.popleft()
    
    if jump < k:
        for d1 in range(4, 12):
            nx, ny = x + dx[d1], y + dy[d1]
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 0 and vis[jump+1][nx][ny] == -1:
                vis[jump + 1][nx][ny] = vis[jump][x][y] + 1
                Q.append((jump+1, nx, ny))
             
    for d2 in range(4):
        nx, ny = x + dx[d2], y + dy[d2]
        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 0 and vis[jump][nx][ny] == -1:
            Q.append((jump, nx, ny))
            vis[jump][nx][ny] = vis[jump][x][y] + 1

ans = []
for a in range(k + 1):
    if vis[a][h -1][w - 1] != -1:
        ans.append(vis[a][h -1][w - 1])

if ans:
    print(min(ans))
else:
    print(-1)

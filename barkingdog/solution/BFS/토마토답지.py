from collections import deque
import sys

m, n = int(input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
queue = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dist = [[0] * m for _ in range(n)]


for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((i, j))
        elif board[i][j] == 0:
            dist[i][j] = -1

while queue:
    x, y = queue.popleft()

    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nx][ny] >= 0:
            continue
        dist[nx][ny] = dist[x][y] + 1
        queue.append((nx, ny))
ans = 0
for i in range(n):
    for j in range(m):
        if dist[i][j] == -1:
            print(-1)
            exit(0)
        ans = max(ans, dist[i][j])

print(ans)





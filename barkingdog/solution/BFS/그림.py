from collections import deque
import sys


n, m = map(int, sys.stdin.readline().split())
vis = [[False] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
queue = deque()
paint = []
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not vis[i][j]:
            count = 1
            queue.append((i, j))
            vis[i][j] = True
            while queue:
                x , y  = queue.popleft()
                for dir in range(4):
                    nx, ny = x + dx[dir], y + dy[dir]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if vis[nx][ny] or board[nx][ny] != 1:
                        continue
                    vis[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
            paint.append(count)

if paint:
    print(len(paint))
    print(max(paint))
else:
    print(0)
    print(0)
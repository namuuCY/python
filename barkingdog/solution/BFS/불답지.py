from collections import deque
import sys

n, m = map(int, input().split())
board = [sys.stdin.readline().rstrip() for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
distf =[[-1]* m for _ in range(n)]
distj =[[-1]* m for _ in range(n)]
jq = deque()
fireq = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 'F':
            fireq.append((i, j))
            distf[i][j] = 0
        elif board[i][j] == 'J':
            jq.append((i, j))
            distj[i][j] = 0

while fireq:
    x, y = fireq.popleft()
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < n and 0 <= ny < m and distf[nx][ny] == -1 and board[nx][ny] != '#':
            fireq.append((nx, ny))
            distf[nx][ny] = distf[x][y] + 1

while jq:
    x, y = jq.popleft()
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            print(distj[x][y] + 1)
            exit(0)
        if distj[nx][ny] >= 0 or board[nx][ny] == '#':
            continue
        if distf[nx][ny] != -1 and distf[nx][ny] <= distj[x][y] + 1:
            continue
        distj[nx][ny] = distj[x][y] + 1
        jq.append((nx, ny))


print("IMPOSSIBLE")
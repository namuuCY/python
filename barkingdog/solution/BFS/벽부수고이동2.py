from collections import deque
import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m, k = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
Q = deque()
vis = [[[False for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
Q.append((0,0,0,1)) #x,y,break횟수, 시간.
for num in range(k + 1):
    vis[0][0][num] = True

while Q:
    x, y, breaknum, s = Q.popleft()
    if x == n - 1 and y == m - 1:
        print(s)
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if board[nx][ny] == 0 and not vis[nx][ny][breaknum]:
            Q.append((nx, ny, breaknum, s + 1))
            vis[nx][ny][breaknum] = True
        if board[nx][ny] == 1 and breaknum < k and not vis[nx][ny][breaknum + 1]:
            Q.append((nx, ny, breaknum + 1, s + 1))
            vis[nx][ny][breaknum + 1] = True
else:
    print(-1)


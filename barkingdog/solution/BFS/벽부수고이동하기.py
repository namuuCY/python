from collections import deque
import sys

n, m = map(int, input().split())           # 이거 자꾸틀리네...
board = [ list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dist = [[[-1, -1] for _ in range(m)] for _ in range(n)]             # 이거 배열 초기화 방법 중요함. 제대로 안하면 오류뜬다
Q = deque()
Q.append((0,0,0))
dist[0][0][0] = dist[0][0][1] = 1

while Q:
    x, y, broken = Q.popleft()
    if x == n - 1 and y == m - 1:
        print(dist[x][y][broken])
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if board[nx][ny] == 0 and dist[nx][ny][broken] == -1:
            Q.append((nx, ny, broken))
            dist[nx][ny][broken] = dist[x][y][broken] + 1
        if not broken and board[nx][ny] == 1 and dist[nx][ny][1] == -1:
            Q.append((nx, ny, 1))
            dist[nx][ny][1] = dist[x][y][broken] + 1
else:
    print(-1)
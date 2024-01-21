from collections import deque
import sys

r, c = map(int, input().split())
board = [sys.stdin.readline().rstrip() for _ in range(r)]
queue = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dist = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if board[i][j] == 'J':
            queue.append((i, j))       # board[][]값은 문자이고
            dist[i][j] = 1                  # 내가 지금 집어넣어야할건 좌표
        elif board[i][j] == 'F':            # 이걸 불이 먼저움직였다고 했더니 맞네
            queue.appendleft((i, j))        # 코드도 사람이짜는데 이사람들아
            dist[i][j] = 9999999
        elif board[i][j] == '#':
            dist[i][j] = 9999999

#if queue[0] == 'F':             # 원래 J,F 둘중 누구먼저일지 판단하는거 생각했는데
#    queue.rotate(1)             # 위에서 J를 appendleft, F를 append하는거로 최적화

while queue:
    x, y = queue.popleft()
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if dist[nx][ny] > 0 :
            continue
        dist[nx][ny] = dist[x][y] + 1
        queue.append((nx,ny))       # 제일중요한 push append를 안해버림

for i in range(r):
    for j in range(c):
        if dist[i][j] == 0:
            dist[i][j] = 9999999
ans = 9999999                     # min값으로 쓰는데 숫자를 너무 작게썻다.. 멍충이
for i in range(r):
    ans = min(ans, dist[i][0], dist[i][c - 1])
for i in range(c):
    ans = min(ans, dist[0][i], dist[r - 1][i])

if ans < 1000000:
    print(ans)
else:
    print('IMPOSSIBLE')





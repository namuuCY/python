from collections import deque
import sys

k = int(input().rstrip())
w, h = map(int, input().split())    # h가 행 개수
board = [ list(map(int, sys.stdin.readline().split())) for _ in range(h)]
dx = [2, 2, 1, 1, -1, -1, -2, -2, 1, 0, -1, 0]
dy = [1, -1, 2, -2, 2, -2, 1, -1, 0, 1, 0, -1]
dist = [[[-1] * w for _ in range(h)] for _ in range(k + 1)]# 횟수 + 1 하는거 자꾸 까먹네
Q = deque()
Q.append((0,0,0))
for l in range(k + 1):          # 횟수 + 1 하는거 자꾸 까먹네
    dist[l][0][0] = 0
ans = []
while Q:                        # 요즘 돌리는거마다 무한루프가 나오네
    jump, x, y = Q.popleft()
    if x == h -1 and y == w-1 and dist[jump][x][y] != -1:
        ans.append(dist[jump][x][y])
    for dir in range(0 if jump < k else 8, 12):
        nx, ny = x + dx[dir], y + dy[dir]
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if board[nx][ny] == 1:
            continue
        if dir >= 8:
            if dist[jump][nx][ny] == -1:
                dist[jump][nx][ny] = dist[jump][x][y] + 1
                Q.append((jump, nx, ny))
            else:
                continue
        elif dir < 8:
            if dist[jump + 1][nx][ny] == -1:
                dist[jump + 1][nx][ny] = dist[jump][x][y] + 1
                Q.append((jump + 1,nx,ny))
            else:
                continue
if ans:
    print(min(ans))
else:
    print(-1)                    #못구했을 경우도 생각해야지

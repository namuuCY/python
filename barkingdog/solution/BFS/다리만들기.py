from collections import deque
import sys

n = int(input().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
vis = [[0]*n for _ in range(n)]
beach = set()
Q = deque()
ISnumber = 0
for i in range(n):          # 섬 구분과 해변가 좌표 체크
    for j in range(n):
        if board[i][j] == 1 and vis[i][j]==0:      # vis체크, beach체크, isnum바꿔주기 체크
            ISnumber += 1
            Q.append((i, j))
            vis[i][j] = 1
            board[i][j] = ISnumber
            while Q:
                x, y = Q.popleft()
                for dir in range(4):
                    nx, ny = x + dx[dir], y + dy[dir]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if board[nx][ny] == 0:
                        beach.add((x, y))
                        continue
                    if vis[nx][ny] == 0 and board[nx][ny] == 1:
                        vis[nx][ny] = 1
                        board[nx][ny] = ISnumber
                        Q.append((nx, ny))
ans = []
for beachpoint in beach:
    xx, yy = beachpoint
    vis = [[0] * n for _ in range(n)]
    vis[xx][yy] = 1
    ISN = board[xx][yy]
    Q.append((xx, yy, 0))
    found = False
    while Q:
        x, y, dist = Q.popleft()
        if found:
            ans.append(dist)
            break
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[nx][ny] != 0 and board[nx][ny] != ISN:
                found = True
                break
            if board[nx][ny] == 0 and vis[nx][ny] == 0:
                vis[nx][ny] = 1
                Q.append((nx, ny, dist + 1))
print(*ans, sep = ' ')

print(min(ans))
            

from collections import deque
import sys

## 이거 0이랑 닿아있는 부분만 색출해서 해당하는 점마다 벽지우고 bfs 돌린건데 시간초과임


input = sys.stdin.readline
n, m = list(map(int, input().split()))        # input은 string이라... 설명이필요한가

board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
Q = deque()
Q.append((0, 0))
dist = [[-1] * m for _ in range(n)]
dist[0][0] = 1
breaking = []
ans = []
def met() -> int:
    while Q:
        x, y  = Q.popleft()
        for i in range(4):
            nx , ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if board[nx][ny] == 1:
                breaking.append((nx, ny))
            if board[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                Q.append((nx, ny))
    return dist[n-1][m-1]

def bfs() -> int:
    while Q:
        x, y  = Q.popleft()
        for i in range(4):
            nx , ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if board[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                Q.append((nx, ny))
    return dist[n-1][m-1]

if met() != -1:
    ans.append(met())

else:
    for cord in breaking:
        x, y = breaking.pop()
        board[x][y] = 0
        Q.append((0, 0))
        dist = [[-1] * m for _ in range(n)]
        dist[0][0] = 1
        if bfs() != -1:
            ans.append(bfs())
        board[x][y] = 1
if ans:
    print(min(ans))
else:
    print(-1)






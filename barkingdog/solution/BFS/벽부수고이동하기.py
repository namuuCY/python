from collections import deque
import sys

input = sys.stdin.readline
n, m = list(map(int, input().split()))        # input은 string이라... 설명이필요한가


board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
Q = deque()
dist = [[-1]* m for _ in range(n)]
Q.append((0, 0))
dist[0][0] = 1

def bfs(x: int, y: int) -> None:        # x,y의 벽을깨고 bfs
    board[x][y] = 0
    Q.append((0, 0))
    while Q:
        x, y = Q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir] , y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and dist[nx][ny] > 0:
                dist[nx][ny] = dist[x][y] + 1
                Q.append((nx, ny))
    board[x][y] = 1
    return dist[n - 1][m - 1]
ans = []
possible = False
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            ans.append(bfs(i, j))
print(*ans )
print(min(ans))


'''
        if board[nx][ny] == 0 and dist[nx][ny] < 1:
            dist[nx][ny] = dist[x][y] + 1
            Q.append((nx, ny))    
        if board[nx][ny] == 1 and breakable:
            for ox in range(2):             # 부술건가 말건가?
                breakable = True
                board[nx][ny] = ox
                if board[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    breakable = False
                                   # 부쉈으면 더이상 사용 불가능
                elif dist[nx][ny] < 1:
                    dist[nx][ny] = dist[x][y] + 1
                    Q.append((nx, ny))
                    break   '''


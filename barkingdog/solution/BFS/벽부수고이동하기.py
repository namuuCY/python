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
breakable = True
while Q:
    x, y = Q.popleft()
    if board[x][y] == 1:
        breakable = False
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] == 1 and breakable:
            dist[nx][ny] = dist[x][y] + 1
            Q.append((nx, ny))
        elif board[nx][ny] == 0 and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            Q.append((nx, ny))

print(dist[n - 1][m - 1])

            


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


from collections import deque
import sys

input = sys.stdin.readline
n, m = list(map(int, input().split()))        # input은 string이라... 설명이필요한가


board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
boQ = deque()
bxQ = deque()
boQ.append((0, 0))
dist = [[0] * m for _ in range(n)]
dist[0][0] = 1
while boQ:
    x, y = boQ.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] == 1:
            for ox in range(2):
                if ox == 1 :
                    break
                else:       # ox가 0, break한것
                    
                    break
        if board[nx][ny] == 0 and dist[nx][ny] == 0:
            dist[nx][ny] = dist[x][y] + 1
            x, y





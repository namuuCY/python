from collections import deque
import sys

trial = int(sys.stdin.readline().rstrip())           # 시간초과나옴...
Q = deque()                            # pypy는 메모리초과도 나옴
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for _ in range(trial):
    m, n = map(int, sys.stdin.readline().split())
    board = [sys.stdin.readline().rstrip() for _ in range(n)]
    time = [[-1]* m for _ in range(n)]      # 현재 모든 점 -1임
    for i in range(n):
        for j in range(m):
            if board[i][j] == '@':
                Q.append((i, j))
                time[i][j] = 0
            elif board[i][j] == '*':        # 불이랑 벽은 9999999
                Q.appendleft((i, j))
                time[i][j] = 9999999
    while Q:
        x, y = Q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] != '#' and time[nx][ny] > 0:
                ftime[nx][ny] = ftime[x][y] + 1
                fq.append((nx, ny))
    '''테두리 '.'인 경우 9999999로 바꾸는것 잊지말기 '''

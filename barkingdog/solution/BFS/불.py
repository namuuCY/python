from collections import deque
import sys

trial = int(sys.stdin.readline().rstrip())           # 시간초과나옴...
fq = deque()                            # pypy는 메모리초과도 나옴
sq = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for _ in range(trial):
    m, n = map(int, sys.stdin.readline().split())
    board = [sys.stdin.readline().rstrip() for _ in range(n)]
    ftime = [[-1]* m for _ in range(n)]
    stime = [[-1]* m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == '@':
                sq.append((i, j))
                stime[i][j] = 0
            elif board[i][j] == '*':
                fq.append((i, j))
                ftime[i][j] = 0
    while fq:
        x, y = fq.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] != '#' and ftime[nx][ny] == -1:
                ftime[nx][ny] = ftime[x][y] + 1
                fq.append((nx, ny))
    
    is_possible = False
    while sq:
        x, y = sq.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                print(stime[x][y] + 1)
                is_possible = True
                break
            elif stime[nx][ny] == -1 and (ftime[nx][ny] > stime[x][y] + 1 or ftime[nx][ny] == -1):  
                sq.append((nx, ny))                 # ftime[nx][ny] == -1 은 추가된거.
                stime[nx][ny] = stime[x][y] + 1
        if is_possible:
            break
    if not is_possible:
        print("IMPOSSIBLE")
        


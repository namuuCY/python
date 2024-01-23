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
            if board[nx][ny] == '#' or time[nx][ny] != -1:
                continue
            time[nx][ny] = time[x][y] + 1
            Q.append((nx, ny))
    ans = 9999999                                 # min값을 구하는거라 초기화값 크게설정해야지
    for a in range(n):                              # 이거처럼 굳이 값을 안바꾸고도 -1일때만 돌아가게끔 하는게 좋음.
        if time[a][0] != -1:
            ans = min(ans, time[a][0])
        if time[a][m - 1] != -1:
            ans = min(ans, time[a][m-1])
    for b in range(m):
        if time[0][b] != -1:
            ans = min(ans, time[0][b])
        if time[n - 1][b] != -1:
            ans = min(ans, time[n - 1][b])
    if ans < 9999999:
        print(ans + 1)                              # 벽에 있는 시간이랑 실제 나가는 값이랑 1차이남.
    else:
        print("IMPOSSIBLE")

    """
    for a in range(n):
        if time[a][0] == -1:
            time[a][0] = 9999999
        if time[a][m - 1] == -1:
            time[a][m - 1] = 9999999
        ans = min(ans, time[a][0], time[a][m - 1])       # 변수 바꿨으면 싹다바꿔야하는데
    for b in range(m):
        if time[0][b] == -1:
            time[0][b] = 9999999
        if time[n-1][b] == -1:
            time[n-1][b] = 9999999
        ans = min(ans, time[0][b], time[n-1][b])
    print(*time, sep='\n')
    
    if ans < 9999999:
        print(ans)
    else:
        print('IMPOSSIBLE')
"""
    '''테두리 '.'인 경우 9999999로 바꾸는것 잊지말기 '''

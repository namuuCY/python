from collections import deque
import sys
                                                # ㅅㅂ 문제는 정직하게 m,n형태로 주지않아
m, n = map(int, input().split())                 # list 형태인거 자꾸까먹
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
numQ = deque()
exeQ = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
days = [[-1] * m for _ in range(n)]


for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            numQ.append((i,j))

while numQ:
    x, y = numQ.popleft()
    days[x][y] = 0                                          
    exeQ.append((x, y))
    vis = [[False] * m for _ in range(n)]       # 매 시작점마다 방문여부가 다르므로 초기화하는것까먹
                                                # 시간초과 뜨기시작함.
    while exeQ:                                 # 시간초과 뜨기시작함.
        x, y = exeQ.popleft()                   # 시간초과 뜨기시작함.
        vis[x][y] = True                        # 시간초과 뜨기시작함.
                                                # 시간초과 뜨기시작함.
        for dir in range(4):
            nx, ny = x + dx[dir] , y + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if vis[nx][ny] or board[nx][ny] == -1 :
                continue
            vis[nx][ny] = True
            if days[nx][ny] == -1:
                days[nx][ny] = days[x][y] + 1
            elif days[nx][ny] > days[x][y] + 1:
                days[nx][ny] = days[x][y] + 1
            exeQ.append((nx, ny))
        
is_valid = True
for i in range(n):
    for j in range(m):
        if not vis[i][j] and board[i][j] == 0:
            is_valid = False
            print(-1)                       # 이부분에서 문제생김
            break                           # else구문은 for 구문이 break없이 되어야 실행인데
if is_valid:                                # 2중 for문이라 안됨.                        
    ans = []
    for i in range(n):
        ans.append(max(days[i]))
    print(max(ans))

    









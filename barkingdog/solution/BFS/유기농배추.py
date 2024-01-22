from collections import deque

trial = int(input().rstrip())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(trial):
    m, n, k = map(int, input().split())     # 또 가로 세로길이 인덱스에 당해버렸다
    board = [[0] * m for _ in range(n)]
    vis = [[False] * m for _ in range(n)]
    count = 0
    Q = deque()
    for _ in range(k):
        a, b = map(int, input().split())
        board[b][a] = 1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not vis[i][j]:
                Q.append((i, j))
                vis[i][j] = True
                count += 1
                while Q:
                    x, y = Q.popleft()
                    for dir in range(4):                                          # 이거 변수 똑같이 i로 써서 혼동되서 틀림
                        nx, ny = x + dx[dir], y + dy[dir]                           # 겹치는 변수 생기면 안됨. 자동적으로 변수 만드는거 xxx
                        if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and board[nx][ny] == 1:
                            vis[nx][ny] = True
                            Q.append((nx, ny))
    print(*board , sep = '\n')
    print(*vis , sep = '\n')

                
    print(count)
        


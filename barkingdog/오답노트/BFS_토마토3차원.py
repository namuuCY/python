from collections import deque
import sys

m, n, h = map(int, input().split())
board = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]
days = [[[-1]* m for _ in range(n)] for _ in range(h)]
Q = deque()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if board[k][i][j] == 1:         # index에러
                days[k][i][j] = 0
                Q.append((k,i,j))

while Q:
    z,x,y = Q.popleft()
    for dir in range(6):
        nx, ny, nz = x + dx[dir], y + dy[dir], z + dz[dir]  #이거 nx ny nz로 안바꾸고 dx dy dz라함 ㅋㅋ
        if  0 <= nx < n and 0 <= ny < m and 0 <= nz <h and \
            board[nz][nx][ny] == 0 and days[nz][nx][ny] == -1 :
            Q.append((nz, nx, ny))                      # 무조건 범위먼저해야함 안그러면 인덱스오류
            days[nz][nx][ny] = days[z][x][y] + 1
ans = 0

for i in range(n):
    for j in range(m):
        for k in range(h):
            if board[k][i][j] == 0 and days[k][i][j] == -1:
                print(-1)
                exit(0)
            else:
                ans = (max(ans, days[k][i][j]))  # days대신 board써버림..

print(ans)




#끝나기 직전에 board 0인 애들중에 days -1 있으면 -1 출력후 종료
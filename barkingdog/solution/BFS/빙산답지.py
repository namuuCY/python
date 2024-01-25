from collections import deque
import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
Q = deque()

def checking(x: int, y: int) -> int:
    count = 0
    for dir in range(4):
        xx, yy = x+ dx[dir],  y+dy[dir]
        if 0 <= xx < n and 0 <= yy < m and ice[xx][yy] ==0:
            count += 1
    return count

def melting() -> None:
    melt = [[0]*m for _ in range(n)]
    for i1 in range(n):
        for j1 in range(m):
            melt[i1][j1] = checking(i1, j1)
    for i2 in range(n):
        for j2 in range(m):
            ice[i2][j2] = max(0, ice[i2][j2]- melt[i2][j2])

def status()-> int:
    cnt1 = sum(ice[i3][j3]>0 for i3 in range(n) for j3 in range(m))               # 이거 이렇게 >0 인것의 개수만 더하는 방법도 있음
    if cnt1 == 0:                                                                   # ice[][] >0 이게 맞으면 1으로 환산되니까
        return 0    # 다녹음
    cnt2 = 0
    a, b = next((i,j) for i in range(n) for j in range(m) if ice[i][j] > 0)   # 이거새로배운 문법두개
    vis = [[0] * m for _ in range(n)]
    Q.append((a,b))
    vis[a][b] = 1
    while Q:
        x, y = Q.popleft()
        cnt2 += 1
        for i4 in range(4):
            nx, ny = x + dx[i4], y+dy[i4]
            if 0<= nx < n and 0<= ny <m and ice[nx][ny] > 0 and vis[nx][ny] == 0:
                vis[nx][ny]=1
                Q.append((nx, ny))
    if cnt1 == cnt2:
        return 1
    else:
        return 2

n, m = map(int, input().split())
ice = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]

year = 0
while True:
    year += 1
    melting()
    icenum = status()
    if icenum == 2:
        print(year)
        break
    elif icenum == 0:
        print(0)
        break
    else:
        continue
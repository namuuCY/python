from collections import deque
import sys

# 빙산 1년 후 높이 함수 / 높이 최댓값함수 /  그점기준 1덩어리인지 bfs 후 그이상있는지 확인 + bfs함수

n, m = map(int, input().split())
ice = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
melting = [[0]*m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

vis =[[0] * m for _ in range(n)]          # 인덱스...
Q = deque()


def MeltAndPoint() -> tuple:
    searched = False
    searched2 = False                        # 이렇게 하면 생각보다 더 빨리 빙산이 녹음
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0:
                for dir in range(4):
                    count = 0
                    ni, nj = i+dx[dir], j+dy[dir]
                    if 0 <= ni < n and 0 <= nj < m:
                        if ice[ni][nj] == 0:
                            count += 1
                    melting[i][j] = count
                    if count == 0 and not searched:
                        point = (i, j)
                        searched = True
    for i1 in range(n):
            for j1 in range(m):
                ice[i1][j1] = max(0, ice[i1][j1]-melting[i1][j1])       # 이런거 사소한 아이디어.
                if ice[i1][j1] > 0 and not searched2:
                    point2 = (i1, j1)
                    searched2 = True

    if searched:
        return point    #점을 순서쌍으로 출력
    elif searched2:
        return point2
    else:
        return
    
def bfs(tup: tuple, viscount: int) -> None:   # 순서쌍 점 기준으로 bfs를 돌려봄
    Q.append(tup)
    tmpx, tmpy = tup
    vis[viscount][tmpx][tmpy] = 1
    while Q:
        x, y = Q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] != 0 and vis[viscount][nx][ny] == 0:
                vis[viscount][nx][ny] = 1
                Q.append((nx, ny))
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0 and vis[viscount][i][j] == 0 :
                return viscount
    return 0            

year = 0

while True:
    year += 1
    point = MeltAndPoint()
    if not point:
        print(0)
        break
    elif bfs(point, year) == year:
        print(year)
        break
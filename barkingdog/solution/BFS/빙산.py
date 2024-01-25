from collections import deque
import sys

# 빙산 1년 후 높이 함수 / 높이 최댓값함수 /  그점기준 1덩어리인지 bfs 후 그이상있는지 확인 + bfs함수

n, m = map(int, input().split())
ice = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
vis = [[[0] * 100 for _ in range(m)] for _ in range(n)]
Q = deque()
def melt() -> tuple:
    searched = False
    for i in range(n):
        for j in range(m):
            if ice[i][j] == 0:
                for dir in range(4):
                    ni, nj = i+dx[dir], j+dy[dir]
                    if ice[ni][nj] != 0:
                        ice[ni][nj] -= 1
            if ice[i][j] != 0 and not searched:
                for dir in range(4):
                    ni, nj = i+dx[dir], j+dy[dir]
                    if ice[ni][nj] == 0:
                        break
                else:
                    searched = True
                    point = (i, j)
    if searched:
        return point    #점을 순서쌍으로 출력
    else:
        

def bfs(tup: tuple, viscount: int) -> None:   # 순서쌍 점 기준으로 bfs를 돌려봄
    Q.append(tup)
    tmpx, tmpy = tup
    vis[viscount][tmpx][tmpy] = 1
    while Q:
        x, y = Q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0<= nx < n and 0 <= ny < m and ice[nx][ny] != 0 and vis[viscount][nx][ny] == 0:
                vis[viscount][nx][ny] = 1
                Q.append((nx, ny))
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0 and vis[viscount][i][j] == 0 :
                return viscount
    return 0            

for year in range(1, 100):




    




        
        
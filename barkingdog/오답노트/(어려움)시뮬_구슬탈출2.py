from collections import deque
import sys

N, M = map(int, input().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
vis = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
            board[i][j] = '.'           # 겹치는 경우까지 고려하는거라 두개의 구슬 위치도 .으로 초기화
        if board[i][j] == 'B':
            bx, by = i, j
            board[i][j] = '.'
dist = [[[[-1] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]  # 남, 오른쪽, 북, 왼쪽
Q = deque()
Q.append((rx, ry, bx, by))      # append할때 tuple잊지말기
dist[rx][ry][bx][by] = 0

def bfs():
    while Q:
        rx, ry, bx, by = Q.popleft()
        if dist[rx][ry][bx][by] >= 10:
            return -1
        for i in range(4):
            nrx, nry, nbx, nby = rx, ry, bx, by     # 주변에 벽있을지 모르니까 아직 바꾸지 말것.
            while board[nbx + dx[i]][nby + dy[i]] == '.':   # 괜히 급하게 먼저 바꿨다가 인덱스에러남.
                nbx += dx[i]
                nby += dy[i]
            if board[nbx + dx[i]][nby + dy[i]] == 'O':
                continue
            while board[nrx + dx[i]][nry + dy[i]] == '.':
                nrx += dx[i]
                nry += dy[i]
            if board[nrx + dx[i]][nry+ dy[i]] == 'O':
                return dist[rx][ry][bx][by] + 1
            if nrx == nbx and nry == nby:
                if i == 0:
                    if rx > bx: nbx -= 1
                    if rx < bx: nrx -= 1
                elif i == 1:
                    if ry > by: nby -= 1
                    if ry < by: nry -= 1
                elif i == 2:
                    if rx > bx: nrx += 1
                    if rx < bx: nbx += 1
                elif i == 3:
                    if ry > by: nry += 1
                    if ry < by: nby += 1
            if dist[nrx][nry][nbx][nby] == -1:
                dist[nrx][nry][nbx][nby] = dist[rx][ry][bx][by] + 1
                Q.append((nrx, nry, nbx, nby))
    return -1           # 답을 찾아서 return하지 못하는 경우도 존재. 
print(bfs())
            









            


            

        

    

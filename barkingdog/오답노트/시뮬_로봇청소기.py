import sys
dx = [-1, 0, 1, 0]   # 0이 북쪽 1동 2남 3서
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
posx, posy, dir = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
vis = [[0] * M for _ in range(N)]
is_exit = False
# 청소 > 판단 > 1) 회전 > 이동
            #  2) 후진

def checking(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if board[nx][ny] == 0 and vis[nx][ny] == 0:
            return True
    return False    # 아무것도 없는경우

def move(order):
    global dir, posx, posy, is_exit
    if order:
        for i in range(1, 5):           # 문제의 조건, 반시계방향회전
            nx, ny = posx + dx[(dir - i) % 4], posy + dy[(dir - i) % 4]
            if board[nx][ny] == 0 and vis[nx][ny] == 0:
                vis[nx][ny] = 1
                posx, posy = nx, ny
                dir = (dir - i) % 4
                return
    else:
        nx, ny = posx - dx[dir], posy - dy[dir]
        if board[nx][ny] == 1:
            is_exit = True
            return
        else:
            posx, posy = nx, ny
            return

vis[posx][posy] = 1

while not is_exit:
    move(checking(posx, posy))

print(sum(vis[i][j] for i in range(N) for j in range(M)))
    
            
    
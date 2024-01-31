import sys

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def roll(order):
    if order == 4:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    if order == 3:
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
    if order == 2:
        dice[4], dice[1], dice[5], dice[3] = dice[1], dice[5], dice[3], dice[4]
    if order == 1:
        dice[5], dice[1], dice[4], dice[3] = dice[1], dice[4], dice[3], dice[5]
    return 

def change(x, y):
    if board[x][y] == 0:
        board[x][y] = dice[3]
        return
    else:
        dice[3] = board[x][y]
        board[x][y] = 0
        return

n, m, x, y, ord = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dice = [0 for _ in range(6)]
order = list(map(int, sys.stdin.readline().split()))

for o in range(ord):
    nx, ny = x + dx[order[o] - 1], y + dy[order[o] - 1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    x, y = nx, ny
    roll(order[o])
    change(x, y)
    print(dice[1])

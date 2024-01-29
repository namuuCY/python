import sys

n, m = map(int, input().split())
board1 = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]     # 이거 어떻게 하는지 확인
board2 = [[0] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cam = []
mn = 0

for i in range(n):
    for j in range(m):
        if board1[i][j] in range(1, 6):
            cam.append((i, j))
        if board1[i][j] == 0:
            mn += 1

def OOB(x, y):
    return x < 0 or y < 0 or x >= n or y >= m   # 이거 범위 제대로 안정해서 idxerr뜸

def upd(x, y, dir):
    dir %= 4
    while True:
        x += dx[dir]
        y += dy[dir]
        if OOB(x, y) or board2[x][y] == 6:
            return
        if board2[x][y] != 0:
            continue
        board2[x][y] = 7

for tmp in range(1 << (2 * len(cam))):
    for i in range(n):
        for j in range(m):
            board2[i][j] = board1[i][j]      # 매 경우의 수마다 새판으로 초기화
    brute = tmp
    for i in range(len(cam)):
        dir = brute % 4
        brute //= 4
        x, y = cam[i]
        if board2[x][y] == 1:               # 들여쓰기 제대로 안함...
            upd(x, y, dir)
        elif board2[x][y] == 2:
            upd(x, y, dir)
            upd(x, y, dir + 2)
        elif board2[x][y] == 3:
            upd(x, y, dir)
            upd(x, y, dir + 1)
        elif board2[x][y] == 4:
            upd(x, y, dir)
            upd(x, y, dir + 1)
            upd(x, y, dir + 2)
        elif board2[x][y] == 5:
            upd(x, y, dir)
            upd(x, y, dir + 1)
            upd(x, y, dir + 2)
            upd(x, y, dir + 3)
    val = sum(board2[i][j] == 0 for i in range(n) for j in range(m))
    mn = min(mn, val)

print(mn)
    






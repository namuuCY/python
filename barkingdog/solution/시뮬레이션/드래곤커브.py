board = [[0]* 101 for _ in range(101)]
N  = int(input().rstrip())      # x,y좌표 또틀림..
# 오른쪽 0 북 1 왼 2 남 3
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
drarr = []
count = 0

def drcommand(g):
    if g == 0:
        drarr.append(0)
    else:
        for i in range(len(drarr)-1, -1, -1):
            drarr.append((drarr[i] + 1) % 4)
    return

def drmove(x, y, d, g):
    board[x][y] += 1
    for i in range(2 ** g):
        x += dx[(drarr[i] + d) % 4]
        y += dy[(drarr[i] + d) % 4]
        board[x][y] += 1

for i in range(11):     # 세대가 i일때 길이는 2의 i제곱
    drcommand(i)

for _ in range(N):
    x, y, d, g = map(int, input().split())
    drmove(y, x, d, g)

for i in range(100):
    for j in range(100):
        if board[i][j] > 0 and board[i][j + 1] > 0 and board[i + 1][j] > 0 and board[i + 1][j + 1] > 0:
            count += 1
print(count)
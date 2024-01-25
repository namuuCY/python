import sys

n = int(input().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white = 0
blue = 0
def is_same(x1: int, y1: int, n1: int):
    for ii in range(x1, x1 + n1):
        for jj in range(y1, y1 + n1):
            if board[x1][y1] != board[ii][jj]:
                return False
    else:
        return True         # 함수에 왜 return을 안써놓지...
#하얀색: 0 / 파란색: 1
def colordiv(x: int, y: int, n2: int):
    global white
    global blue
    if is_same(x, y, n2):
        if board[x][y] == 0:
            white += 1
        elif board[x][y] == 1:
            blue += 1
    else:
        m = n2 // 2
        if m > 0:                   # m값이 0이 될수 있다.
            for i in range(x, x + n2, m):
                for j in range(y, y + n2, m):
                    colordiv(i, j, m)

colordiv(0, 0, n)
print(white)
print(blue)


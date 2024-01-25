import sys

n = int(input())
board = [['*'] * n for _ in range(n)]

def star(x: int, y: int, n: int):
    m = n // 3
    while m > 0:
        if (x // m) % 3 == 1 and (y // m) % 3 == 1:
            board[x][y] = ' '
        m //= 3

for i in range(n):
    for j in range(n):
        star(i, j, n)
for i in range(n):
    print(*board[i], sep = '')

                

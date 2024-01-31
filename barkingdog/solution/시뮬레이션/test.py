from copy import deepcopy
import sys
from math import factorial

for i in range(8):
    print(factorial(13) // (factorial(i)* factorial(13-i)))


'''
n = int(input().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 0


def execute(dir):
    global board2
    if dir == 0:
        for i in range(n):
            tmp = []
            is_next = True
            for j in range(n):
                if board2[i][j] != 0:
                    if is_next:
                        tmp.append(board2[i][j])
                        is_next = False
                    else:
                        if tmp[-1] == board2[i][j]:
                            tmp[-1] *= 2
                            is_next = True
                        else:
                            tmp.append(board2[i][j])
                            is_next = False
            for _ in range(n - len(tmp)):
                tmp.append(0)
            board2[i] = tmp.copy()
    if dir == 1:
        tmp = deepcopy(board2)
        board2 = [list(row) for row in zip(*tmp)]
        execute(0)
        tmp = deepcopy(board2)
        board2 = [list(row) for row in zip(*tmp)]
    if dir == 2:
        for i in range(n):
            board2[i].reverse()
        execute(0)
        for i in range(n):
            board2[i].reverse()
    if dir == 3:
        for i in range(n):
            board2[i].reverse()
        execute(1)
        for i in range(n):
            board2[i].reverse()

board2 = deepcopy(board)
execute(1)
print(*board2, sep = '\n')
'''
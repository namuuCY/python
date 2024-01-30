from copy import deepcopy
import sys


n = int(input().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 4진법 써먹어보자.

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def lift(dir):
    if dir == 0:    
        for i in range(n):
            for j in range(n):
                if i == 0:
                

for trial in range(4**5):
    board2 = deepcopy(board)
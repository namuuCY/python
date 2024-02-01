import sys
from copy import deepcopy

N, M = map(int, input().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
vis = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j




            


            

        

    

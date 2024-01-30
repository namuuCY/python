from copy import deepcopy
import sys


n = int(input().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 0
# 4진법 써먹어보자.


       

for trial in range(4**5):
    board2 = deepcopy(board)

    ans = max(ans, max(board2[i][j] for i in range(n) for j in range(n)))
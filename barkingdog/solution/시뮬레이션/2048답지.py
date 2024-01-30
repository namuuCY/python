from copy import deepcopy
import sys

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
            for _ in range(n - len(tmp)):       # tmp의 길이만큼 채워야..3
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
        tmp = deepcopy(board2)
        board2 = [list(row) for row in zip(*tmp)]
        execute(2)
        tmp = deepcopy(board2)
        board2 = [list(row) for row in zip(*tmp)]
    
for tmp in range(4**5):
    board2 = deepcopy(board)
    for _ in range(5):
        dir = tmp % 4
        tmp //= 4
        execute(dir)
    ans = max(ans, max(board2[i][j] for i in range(n) for j in range(n)))

print(ans)

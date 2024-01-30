from copy import deepcopy
import sys


n = int(input().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 0
# 4진법 써먹어보자.
# 더하고 당기면 된다.

def lift(dir):
    global board2
    if dir == 0:
        for i in range(n):  # i는 고정, j만 움직임
            idx = 0
            cnt = board2[i].count(0)
            for _ in range(cnt):
                board2[i].remove(0)
            for j in range(idx, len(board2[i]) - 2):
                if board2[i][j] == board2[i][j + 1]:
                    board2[i][j] += board2[i][j + 1]
                    board2[i].remove(board2[i][j + 1])
                    if j + 1 == len(board2[i]) - 1:
                        break           
            for _ in range(n - len(board2[i])):
                board2[i].append(0)
    if dir == 1:
        tmp = deepcopy(board2)
        board2 = [list(row) for row in zip(*tmp)]
        lift(0)
        tmp = deepcopy(board2)
        board2 = [list(row) for row in zip(*tmp)]
    if dir == 2:
        for i in range(n):
            board2[i] = board2[i][::-1]
        lift(0)
        for i in range(n):
            board2[i] = board2[i][::-1]
    if dir == 3:
        tmp = deepcopy(board2)
        board2 = [list(row) for row in zip(*tmp)]
        lift(2)
        tmp = deepcopy(board2)
        board2 = [list(row) for row in zip(*tmp)]

for trial in range(4**5):
    board2 = deepcopy(board)
    for _ in range(5):
        dir = trial % 4
        trial //= 4
        lift(dir)

    ans = max(ans, max(board2[i][j] for i in range(n) for j in range(n)))

print(ans)
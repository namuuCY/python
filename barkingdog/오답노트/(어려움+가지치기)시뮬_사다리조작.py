# 이거 답이 맞긴 할건데 시간초과임.

from itertools import combinations
import sys
# N이 세로선 개수 H가 점선개수
N, M, H = map(int, input().split())
board = [[0] * (N + 1) for _ in range(H + 1)]

for _ in range(M):
    t1, t2 = map(int, input().split())
    board[t1][t2] = 1
           # 사다리에 홀수인게 있으면 그만큼 더해줘야 가능성이 있어서 이것도 가지치기


def ck():
    for i in range(1, N):       # N-1번째까지만 하면 마지막건 자동이라 가지치기
        now = i
        for j in range(1, H + 1):
            if board[j][now] == 1:
                now += 1
            elif board[j][now - 1] == 1:
                now -= 1
        if now != i:
            return False
    return True

def recur(n, x, y):
    global ans
    if n >= ans:                            # 이거 해주면 빠름
        return
    if ck():
        ans = min(ans, n)
        return 
     # 사다리에 홀수인게 있으면 그만큼 더해줘야 가능성이 있어서 이것도 가지치기
    for i in range(x, H + 1):                   # 효율적인 가지치기 2 : 다음 사다리의 범위 제한시키기
        for j in range(y if x==i else 1, N):
            if board[i][j - 1] == 1 or board[i][j] == 1 or board[i][j + 1] == 1:
                continue
            board[i][j] = 1
            recur(n + 1, i, j + 2)              # 효율적인 가지치기 3 : 다음 사다리의 범위 제한시키기
            board[i][j] = 0

ans = 4
recur(0, 1, 1)
print(ans if ans != 4 else -1)

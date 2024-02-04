# 이거 답이 맞긴 할건데 시간초과임.

from itertools import combinations
import sys
# N이 세로선 개수 H가 점선개수
N, M, H = map(int, input().split())
board = [[0] * N for _ in range(H)]
for _ in range(M):
    t1, t2 = map(int, sys.stdin.readline().split())
    board[t1 - 1][t2 - 1] = 1


def exchange():
    nums = list(range(N))
    nums2 = list(range(N))
    for i in range(H):
        for j in range(N - 1):
            if board[i][j] == 1:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    for i in range(N):
        if nums[i] != nums2[i]:
            return False
    return True

def recur(n):
    global ans
    if exchange():
        ans = min(ans, n)
        return 
    if n == 3:
        return
    if n >= ans:
        return
    for i in range(H):
        for j in range(N - 1):
            if board[i][j] == 1:
                continue
            if j - 1 in range(N - 1) and board[i][j - 1] == 1:
                continue
            if j + 1 in range(N - 1) and board[i][j + 1] == 1:
                continue
            board[i][j] = 1
            recur(n + 1)
            board[i][j] = 0
ans = 4
recur(0)
print(ans if ans != 4 else -1)

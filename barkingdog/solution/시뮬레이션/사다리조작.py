from itertools import combinations
import sys
# N이 세로선 개수 H가 점선개수
N, M, H = map(int, input().split())
board = [[0] * N for _ in range(H)]
for _ in range(M):
    t1, t2 = map(int, sys.stdin.readline().split())
    board[t1 - 1][t2 - 1] = 1


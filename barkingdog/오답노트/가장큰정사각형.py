import sys
N, M = map(int, input().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
DP = [[]]
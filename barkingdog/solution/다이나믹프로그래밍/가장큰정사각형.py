import sys
N, M = map(int, input().split())        # N행 M열
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
DP = {}

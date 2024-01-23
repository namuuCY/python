from collections import deque
import sys

input = sys.stdin.readline()
n, m = map(int, input().split())         # input은 string이라... 설명이필요한가

board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
print(*board, sep = '\n')
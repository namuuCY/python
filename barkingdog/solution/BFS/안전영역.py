from collections import deque
import sys

dir = [[1,0], [0, 1], [-1, 0], [0, -1]]
Q = deque()



n = int(input().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

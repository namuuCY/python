from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip)) for _ in range(n)]
Q = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dist = [[-1]*m for _ in range(n)]
Q.append((0, 0))
dist[0][0] = 1
while Q:
    x, y = Q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
from collections import deque
import sys

k = int(input().rstrip())
w, h = map(int, input().split())    # h가 행 개수
board = [ list(map(int, sys.stdin.readline().split())) for _ in range(h)]
dx = [1, 0, -1, 0, 2, 2, 1, 1, -1, -1, -2, -2]
dy = [0, 1, 0, -1, 1, -1, 2, -2, 2, -2, 1, -1]
dist = [[[-1] * w for _ in range(h)] for _ in range(k)]
Q = deque()
Q.append((0,0,0))
for l in range(k):
    dist[l][0][0] = 0
while Q:
    jump, x, y = Q.popleft()
    

print(dist[][h-1][w-1])

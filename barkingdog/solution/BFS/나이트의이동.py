from collections import deque
import sys
trial = int(input().rstrip())
dx = [2, 2, 1, 1, -1, -1, -2, -2,]
dy = [1, -1, 2, -2, 2, -2, 1, -1]
Q = deque()

for _ in range(trial):
    l = int(input().rstrip())
    vis = [[0]* l for _ in range(l)]
    pos = map(int, input().split())
    des = map(int, input().split())
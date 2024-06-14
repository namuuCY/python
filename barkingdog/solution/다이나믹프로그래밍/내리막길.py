import sys
from collections import deque

# 방식은 맞으나 시간초과. 너무 많이 중복되는 경로가 생겨서 문제임.
# DP 를 제대로 이용하지 못함.

def OOB(x, y):
    return x < 0 or x >= N or y < 0 or y >= M

def BFS(x, y):
    DP[x][y] = 1
    Q.append((x, y))
    while Q:
        cx, cy = Q.popleft()
        for dir in range(4):
            nx, ny = cx + dx[dir], cy + dy[dir]
            if OOB(nx, ny) or heights[nx][ny] >= heights[cx][cy] : continue
            DP[nx][ny] += 1
            Q.append((nx, ny))

input = sys.stdin.readline
N, M = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
DP = [[0 for _ in range(M)] for _ in range(N)]
Q = deque()

BFS(0, 0)

print(DP[N - 1][M - 1])

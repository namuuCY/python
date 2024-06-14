import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.read
data = input().split()
idx = 0
N, M = int(data[0]), int(data[1])
idx += 2
height = [[0 for _ in range(M)] for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        height[i][j] = int(data[idx])
        idx += 1

DP = [[-1 for _ in range(M)] for _ in range(N)]

def func(x, y):
    if x == N - 1 and y == M - 1 :
        DP[x][y] = 1
        return 1
    if DP[x][y] == -1:
        DP[x][y] = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if height[x][y] <= height[nx][ny] : continue
            DP[x][y] += func(nx, ny)
        
    return DP[x][y]
        
print(func(0, 0))


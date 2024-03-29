from collections import deque
import sys

input = sys.stdin.readline

def bfs(a: int, b: int) -> int:
    Q.append((a, b))
    area = 1
    while Q:
        x, y = Q.popleft()
        for d in range(4):
            nx, ny = x + dir[d][0], y + dir[d][1]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                Q.append((nx, ny))
                board[nx][ny] = 1
                area += 1
    return area

m, n, k = list(map(int, input().split()))
board = [[0] * m for _ in range(n)]
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
Q = deque()
area = []
count = 0
for _ in range(k):
    x1, y1, x2, y2 = list(map(int, input().split()))
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1


for x in range(n):
        for y in range(m):
            if board[x][y] == 0:
                count += 1
                board[x][y] = 1             # vis 함수를 안쓸거면 이거라도 제대로 마킹하셈
                area.append(bfs(x,y))
area.sort()
print(count)
print(*area, sep = ' ')



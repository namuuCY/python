from collections import deque
import sys

n, m = map(int, input().split())        # map(함수, iterable) 이래야한다고!
board = [sys.stdin.readline().rstrip() for _ in range(n)]
dist = [[- 1] * m for _ in range(n)]        # 이문제 조심해야할점.
dx = [1, 0, -1, 0]                      # 미로를 1과0으로 표시했는데 띄어쓰기안함 ㅅㅂ
dy = [0, 1, 0, -1]                      # sys.stdin~~ 는 str 이다! 그래서 []한번 더 안해도됨
queue = deque()                     # 맨처음 썼던거
queue.append((0, 0))                # [[list(map(int, sys.stdin.readline().split()))] for _ in range(n)]
dist[0][0] = 1
while queue:
    x, y = queue.popleft()
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nx][ny] != -1 or board[nx][ny] != '1':    # index error뜸 nx,ny 범위벗어남
            continue
        dist[nx][ny] = dist[x][y] + 1
        queue.append((nx, ny))


print(dist[n - 1][m - 1])
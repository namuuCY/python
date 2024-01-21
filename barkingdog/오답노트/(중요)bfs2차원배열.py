from collections import deque

board = [
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

n, m = 7, 10
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
vis = [[False for _ in range(m)] for _ in range(n)]

queue = deque()
queue.append((0,0))
vis[0][0] = True

while queue:
    cur = queue.popleft()
    print(f'({cur[0]}, {cur[1]}) -> ', end = '')
    for dir in range(4):
        nx, ny = cur[0] + dx[dir], cur[1] + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if vis[nx][ny] or board[nx][ny] != 1:
            continue
        vis[nx][ny] = True
        queue.append((nx, ny))
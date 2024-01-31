from collections import deque
import sys

dummy = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(12)]
board = [list(row) for row in zip(*dummy[::-1])]    # dummy 회전시켜서 6행 12열
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
Q = deque()
chain = 0
vis = [[0] * 12 for _ in range(6)]

# BFS 검사후 4개 이상이면 터트리는 함수 - 여러그룹이 터지더라도 한번에 터지고 1연쇄임
# 터트린후에 아래로 밀어버리는 함수
def popping():
    global vis, is_pop
    vis = [[0] * 12 for _ in range(6)]
    is_pop = False
    for i in range(6):
        for j in range(12):
            if board[i][j] != '.' and vis[i][j] == 0:
                tmp = []
                Q.append((i, j))
                tmp.append((i, j))
                vis[i][j] = 1
                count = 0
                while Q:
                    x, y = Q.popleft()
                    count += 1
                    tmp.append((x, y))
                    for dir in range(4):
                        nx, ny = x + dx[dir], y + dy[dir]
                        if nx < 0 or nx >= 6 or ny < 0 or ny >= 12:
                            continue
                        if vis[nx][ny] == 0 and board[nx][ny] == board[x][y]:
                            vis[nx][ny] = 1
                            Q.append((nx, ny))
                if count >= 4:
                    is_pop = True
                    for (x, y) in tmp:
                        board[x][y] = '.'   # chain값은?

def lift():
    global board
    for i in range(6):
        tmp = []
        for j in range(12):
            if board[i][j] != '.':
                tmp.append(board[i][j])
        for _ in range(12 - len(tmp)):
            tmp.append('.')
        board[i] = tmp

is_pop = True
while is_pop:
    popping()
    if is_pop:
        chain += 1
    lift()

print(chain)
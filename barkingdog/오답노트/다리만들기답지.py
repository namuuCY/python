from collections import deque
import sys

n = int(input().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
vis = [[0] * n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
Q = deque()

def check(x: int, y: int):               # 범위 내 체크
    return 0 <= x < n and 0 <= y < n

# 섬 별로 이름 지어주기
def island():
    isnum = 1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and vis[i][j] == 0:
                board[i][j] = isnum
                Q.append((i, j))
                vis[i][j] = 1
                while Q:
                    x, y = Q.popleft()
                    for dir in range(4):
                        nx, ny = x + dx[dir], y + dy[dir]
                        if check(nx, ny) and vis[nx][ny] == 0 and board[nx][ny] == 1:
                            board[nx][ny] = isnum
                            vis[nx][ny] = 1
                            Q.append((nx, ny))
                isnum += 1
    return

island()        # 함수 만들어두고 실행을 안함 ㅋㅋ
vis = [[-1] * n for _ in range(n)]
for i in range(n):
    for j in range(n):                  # 모든 육지의 섬들을 다 집어넣고 bfs돌림
        if board[i][j] != 0:            # 이때, 같은 이름의 섬이 다음 점으로 잡히면 해당하는점은 continue로 패스함
            Q.append((i, j))            # 또, 바다를 만나면 만나는 바다를 인접 섬의 이름으로 바꿔버림
            vis[i][j] = 0               # 두개의 섬이 확장하면서 만나는 상황이 생기면 이때 이전의 점(x,y)에서의 거리와 현재 점(xx,yy)에서의 거리의 합이 다리의 길이가됨
                                        # 그리고 이건 끝날때까지 계속하는거라 min값을 챙겨야함.
ans = 999999
while Q:
    x, y = Q.popleft()
    for di in range(4):
        xx, yy = x + dx[di], y + dy[di]
        if not check(xx, yy) or board[xx][yy] == board[x][y]:
            continue
        if board[xx][yy] != 0:
            ans = min(ans, vis[xx][yy] + vis[x][y])
        else:
            board[xx][yy] = board[x][y]
            vis[xx][yy] = vis[x][y] + 1
            Q.append((xx, yy))

print(ans)




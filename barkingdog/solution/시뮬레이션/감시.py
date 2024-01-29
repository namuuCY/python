n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cam = []
count = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
tmp = []
ans = 64
def surveil(i):      # i + 1번째 카메라
    global count, ans
    if i == len(cam):
        for i1 in range(n):
            for j1 in range(m):
                if board[i1][j1] == 0:
                    count += 1
        ans = min(ans, count)
        print(*board, sep = '\n')
        print()
        count = 0
        return
    for dir in range(4):
        x, y = cam[i]
        sight(board[x][y], dir, x, y)
        for k1 in range(len(tmp)):
            board[tmp[k1][0]][tmp[k1][1]] -= 1
        tmp1 = tmp
        tmp.clear()
        surveil(i + 1)
        for k1 in range(len(tmp1)):
            board[tmp1[k1][0]][tmp1[k1][1]] += 1
        tmp1.clear()

def sight(j, dir, x, y):  #j는 카메라 번호, #dir은 방향()
    for a in range(1, n):
        nx, ny = x + a * dx[dir % 4], y + a * dy[dir % 4]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            break
        if board[nx][ny] == 6:
            break
        if board[nx][ny] == 0:
            tmp.append((nx, ny))
    if j == 3 or j == 4 or j == 5:
        for a in range(1, n):
            nx, ny = x + a * dx[(dir+1) % 4], y + a * dy[(dir+1) % 4]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            if board[nx][ny] == 0:
                tmp.append((nx, ny))
    if j == 2 or j == 4 or j == 5:
        for a in range(1, n):
            nx, ny = x + a * dx[(dir+2) % 4], y + a * dy[(dir+2) % 4]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            if board[nx][ny] == 0:
                tmp.append((nx, ny))
    if j == 5:
        for a in range(1, n):
            nx, ny = x + a * dx[(dir+3) % 4], y + a * dy[(dir+3) % 4]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            if board[nx][ny] == 0:
                tmp.append((nx, ny))

for i in range(n):
    for j in range(m):
        if board[i][j] in range(1, 6):
            cam.append((i, j))
if cam:
    surveil(0)
    print(ans)
else:
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                count += 1
    print()


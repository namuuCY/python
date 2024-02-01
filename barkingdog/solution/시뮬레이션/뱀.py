from collections import deque

N = int(input().rstrip())
board = [[0] * N for _ in range(N)]
K = int(input().rstrip())
for _ in range(K):
    i, j = map(int, input().split())    # 사과 위치 -1 씩 빼는거...
    board[i - 1][j - 1] = 2
L = int(input().rstrip())
order = {}
for _ in range(L):                  # 시간 따라서 어떻게 구현하는지 팁없냐
    X, C = map(str, input().split()) 
    x = int(X)
    c = 1 if C == 'D' else -1
    order[x] = c

def EOG(x, y):
    global is_exit
    if x < 0 or y < 0 or x >= N or y >= N or board[x][y] == 1:
        is_exit = True
        return True
    else: return False

dx = [0, 1, 0, -1]  # 0이 동쪽 dir증가하면 오른쪽 90도 감소하면 왼쪽 90도
dy = [1, 0, -1, 0]
posx, posy = 0, 0
Q = deque()
Q.append((posx, posy))
dir = 0
board[posx][posy] = 1
time = 0
is_exit = False

while not is_exit:
    time += 1
    posx, posy = posx + dx[dir], posy + dy[dir]
    if EOG(posx, posy):
        break
    if board[posx][posy] == 2:
        board[posx][posy] = 1
        Q.append((posx, posy))
    elif board[posx][posy] == 0:
        board[posx][posy] = 1
        Q.append((posx, posy))
        tx, ty = Q.popleft()
        board[tx][ty] = 0
    if time in order:
        dir = (dir + order[time]) % 4

print(time)
    

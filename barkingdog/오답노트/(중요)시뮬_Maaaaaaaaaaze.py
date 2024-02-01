from collections import deque
import sys
from copy import deepcopy
from itertools import permutations

dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]
Q = deque()
board = []
for i in range(5):
    board.append([list(map(int, sys.stdin.readline().split())) for _ in range(5)])

def rot(num, dir):
    global board
    new_board = deepcopy(board[num])        # board값 바꿀때 board=board식으로 써넣으면 제대로 안됨
    if dir == 0:
        return
    elif dir == 1:
        for i in range(5):
            for j in range(5):
                board[num][i][j] = new_board[4 - j][i]
        return
    elif dir == 2:
        for i in range(5):
            for j in range(5):
                board[num][i][j] = new_board[4 - i][4 - j]
        return
    else:
        for i in range(5):
            for j in range(5):
                board[num][i][j] = new_board[j][4 - i]
        return

def OOB(x, y, z):
    return x<0 or y<0 or z<0 or x>=5 or y>=5 or z>=5

def BFS(x, y, z, c):
    dist = [[[-1]* 5 for _ in range(5)] for _ in range(5)]
    dist[0][0][0] = 0
    Q.append((x, y, z))
    while Q:
        x, y, z= Q.popleft()                    # 함수에 board나 c가 들어갈때는 인자로 넣어주기
        for dir in range(6):
            nx, ny, nz = x + dx[dir], y + dy[dir], z + dz[dir]
            if OOB(nx, ny, nz) or c[nx][ny][nz] == 0 or dist[nx][ny][nz] >= 0:
                continue
            dist[nx][ny][nz] = dist[x][y][z] + 1
            Q.append((nx, ny, nz))                  ## -1이 계속 나올때와 답이 계속 나올때가 섞이니까 이거 생각
    return dist[4][4][4] if dist[4][4][4] != -1 else 200

 # comb의 원소는 board0~4까지 순서대로 섞인거
ans = 200

for tmp in range(4**5):                 # 들여쓰기 엄청중요함. 들여쓰기좀 똑바로 볼필요있다.
    tmp1 = tmp
    for plate in range(5):
        dir = tmp1 % 4
        tmp1 //= 4
        rot(plate, dir)
        comb = list(permutations(board, 5))
        for c in comb:
            if c[0][0][0] == 0 or c[4][4][4] == 0:
                continue
            tmpans = BFS(0,0,0,c)       
            if tmpans == 12:            # 12는 무조건 최솟값이니까 이거 발견하면 즉시종료
                print(12)
                exit(0)
            ans = min(ans, tmpans)      # -1이 계속 나올때와 답이 계속 나올때가 섞이니까 이거 생각
            
if ans == 200:
    print(-1)
else:
    print(ans)
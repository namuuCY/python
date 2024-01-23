from collections import deque
import sys

## 문제 총평 : 다른 사람 풀이에서 시간을 따로 계산해서


dir = [[1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1]]

while True:                                             # 입력값이 너무 ㅈ같은경우!
    L, R, C = map(int, sys.stdin.readline().split())
    if L == 0 and R == 0 and C == 0:
        break
    maze = []
    Q = deque()

    for _ in range(L):
        layer = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
        maze.append(layer)
        sys.stdin.readline()            # 빈줄 읽어넘기기
    
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if maze[i][j][k] == 'S':
                    s = 0
                    Q.append((i, j, k, s))


    is_possible = False
    
    while Q:
        x, y, z, s = Q.popleft()
        for a in range(6):
            nx, ny, nz = x + dir[a][0], y + dir[a][1], z + dir[a][2]
            if nx<0 or nx>= L or ny <0 or ny >= R or nz<0 or nz>=C:
                continue
            if maze[nx][ny][nz] == 'E':
                is_possible = True
                print(f"Escaped in {s + 1} minute(s).")
            if maze[nx][ny][nz] == '.' or maze[nx][ny][nz] == 'E':
                Q.append((nx, ny, nz, s+1))         # append할때 tuple()
                maze[nx][ny][nz] = 'S'

    if not is_possible:
        print('Trapped!')

"""    while Q:
        x, y, z, s = Q.popleft()
        if maze[x][y][z] == 'E':                # 내가한거: S가 지나간 maze값을 죄다 'S'로 바꿔놓음. 이때 E도 바뀐뒤에 if 구문을 실행하는 거라 문제가생김
            print(f'Escaped in {s} minute(s).') # 'S'로 바꾼이유: 내가 지나갔다는 걸 표시하기위해서. 이러면 visit 이라는 2차원 불린배열을 만들지 않아도 되고, Q에 시간을 추가만해도 됨
            break
        maze[x][y][z] = 'S'                               #              그대신 
        for a in range(6):
            nx, ny, nz = x + dir[a][0], y + dir[a][1], z + dir[a][2]     # dir는 2차원배열이잖아
            if nx < 0 or nx >= L or ny < 0 or ny >= R or nz < 0 or nz >= C:
                continue
            if maze[nx][ny][nz] != '.':         # 이 조건 하나만 두는거 위험한게 저 메이즈 값이 E인걸 놓치고있음
                continue                        
            Q.append((nx, ny, nz, s + 1))
            
    else:
        print('Trapped!') """
    
        



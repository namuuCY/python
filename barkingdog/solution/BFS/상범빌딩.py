from collections import deque
import sys

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
                if maze[i][j][k] == 'E':
                    des = [i, j, k]
    
    while Q:
        x, y, z, s = Q.popleft()
        for a in range(6):
            nx, ny, nz = x + dir[a][0], y + dir[a][1], z + dir[a][2]
            if nx<0 or nx>= L or ny <0 or ny >= R or nz<0 or nz>=0:
                continue
            if maze[nx][ny][nz] != '.':
                continue
            if nx == 
            Q.append(nx, ny, nz, s+1)
            maze[nx][ny][nz] = 'S'

        

            # maze값 S로 만드는거, s값 1추가하는거



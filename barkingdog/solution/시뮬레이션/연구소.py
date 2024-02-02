from collections import deque
from itertools import combinations
from copy import deepcopy
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
walls = []
Q = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
safe = 0
vlist = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            walls.append((i, j))
            safe += 1
        if board[i][j] == 2:
            vlist.append((i, j))  
combs = list(combinations(walls, 3))        
'''가지치기 다시생각하자.
                    '''
def BFS():
    global board2
    virus = 0
    for i in vlist:
        Q.append(i)
    while Q:        # 큐를 전부 써버리니까 큐도 초기화가 되버림. 그래서 안되던거
        x, y = Q.popleft()
        for dir in range(4):
            if virus > min_virus:
                return 9999
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < N and 0 <= ny < M and board2[nx][ny] == 0:
                board2[nx][ny] = 2
                Q.append((nx, ny))
                virus += 1          # 초기 바이러스 위치 n개가 빠진게 safe 계산할때 들어갔는데 그걸 까먹음
    return virus
ans = 0
min_virus = 9999
for threewall in combs:
    board2 = deepcopy(board)
    for tw in threewall:
        i, j = tw
        board2[i][j] = 1
    virus = BFS()
    min_virus = min(min_virus, virus)
    tmp = safe - 3 - virus
    ans = max(ans, tmp)

print(ans)
    


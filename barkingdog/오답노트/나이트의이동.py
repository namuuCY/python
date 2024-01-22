from collections import deque
import sys
trial = int(input().rstrip())
dx = [2, 2, 1, 1, -1, -1, -2, -2,]
dy = [1, -1, 2, -2, 2, -2, 1, -1]
Q = deque()

for _ in range(trial):
    l = int(input().rstrip())
    dist = [[-1] * l for _ in range(l)]
    pos = list(map(int, input().split()))     # map = list 아님... 
    des = list(map(int, input().split()))
    if pos == des:
        print(0)
        continue     # pos = des 일 경우도 고려해야함.
    Q.append(pos)
    dist[pos[0]][pos[1]] = 0
    while Q:
        x, y = Q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx == des[0] and ny == des[1]:
                print(dist[x][y] + 1)
                while Q:
                    Q.pop()          # 이거 pop할게 남아서 계속 돌리고있네
                break                        # 이거 3번 돌려야하는데 exit 하면안되지...
            if 0 <= nx < l and 0 <= ny < l and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                Q.append((nx, ny))     



    

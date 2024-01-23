from collections import deque
import sys
# 힌트 이용 안함. 아무지역도 안잠기는경우 -> 1
# 밑에 주석된부분 보기바람
ans = []
n = int(input().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]        
dir = [[1,0], [0, 1], [-1, 0], [0, -1]]                                         
Q = deque()

def bfs(h: int) -> int:
    vis = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > h and not vis[i][j]:
                Q.append((i, j))
                count += 1 
                while Q:
                    x, y = Q.popleft()
                    for d in range(4):
                        nx, ny = x + dir[d][0], y + dir[d][1]
                        if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and board[nx][ny] > h:
                            Q.append((nx, ny))
                            vis[nx][ny] = True
    return count
limit = 0    
for i in range(n):
    limit = max(limit, max(board[i]))

for i in range(limit + 1):
    ans.append(bfs(i))

print(max(ans))
    


'''height = set([0, 1])            # set은 append가 아니라 add사용함.
                                # set(~)    ~에 들어갈 인자는 iterable객체여야함
for i in range(n):                  어차피 100번 안이라 최대 높이만 재고 물깊이는 0부터 시작해도 됨.
    for j in range(n):              이거처럼 원소의 값만 집어넣으면 경우의 수가 전부 다 세어지지는 않음.
        height.add(board[i][j])

for h in height:
    ans.append(bfs(h))

print(max(ans))        '''
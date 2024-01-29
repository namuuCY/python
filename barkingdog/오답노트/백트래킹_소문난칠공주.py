from collections import deque
from itertools import combinations

# 7명, 최소 4명이 이다솜파(S)
board = [list(map(str, input().rstrip())) for _ in range(5)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = 0

def check(comb):
    vis = [[False]* 5 for _ in range(5)]
    Q = deque([comb[0]])            # deque()에는 iterable이 들어와야함
    vis[comb[0][0]][comb[0][1]] = True
    adj = 0     # 인접한게 맞을때 +
    ds = 0      # 이다솜파가 맞을때 +
    while Q:
        x, y = Q.popleft()
        adj += 1
        if board[x][y] == 'S':
            ds += 1
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < 5 and 0 <= ny < 5 and not vis[nx][ny] and (nx, ny) in comb:
                vis[nx][ny] = True
                Q.append((nx, ny))
    return adj >= 7 and ds >= 4

for comb in combinations([(i, j) for i in range(5) for j in range(5)], 7):  # 이 표현 자주쓴다
    ans += check(comb)

print(ans)

'''
def infseven(k, x, y):          # 중복되는거 어떻게 처리할거?   /   한줄이 아닌경우 어떻게 처리할꺼?
    global count                # 임의로 7개 선발후에 인접한거를 찾을까?     계산해보니 48만개정도나옴
    if k == 7:
        if ans.count('S') >= 4:     # 지금 이거 ans의 개수와 k의 값이 맞지않는다.
            count += 1
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5 and not vis[nx][ny]:
            vis[nx][ny] = True
            ans.append(board[nx][ny])
            infseven(k + 1, nx, ny)
            vis[nx][ny] = False
            ans.pop()


for i in range(5):          # S로 시작되는거부터 할까? 이러면 줄긴하는데
    for j in range(5):
        vis[i][j] = True
        ans.append(board[i][j])
        infseven(0, i, j)
        vis[i][j] = False
        ans.pop()

print(count)
'''
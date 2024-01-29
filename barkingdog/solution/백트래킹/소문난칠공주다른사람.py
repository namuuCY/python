from collections import deque

def recur(adj, yds, ans_set):
    if adj == 4 and yds == 0 :
        return
    if adj == 5 and yds <= 1:
        return
    if adj == 6 and yds <= 2:
        return
    if adj == 7:
        if yds >= 4:
            ans_set = frozenset()
            ans_comb.add(ans_set)

    for j in range(len(ans_set)):
        x, y = ans_set[j]
        for dir in range(4):
            nx, ny = x+ dx[dir], y+ dy[dir]
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in ans_set and not vis[nx][ny]:
                ans_set.append((nx, ny))
                if board[nx][ny] == "S":
                    recur(adj + 1, yds + 1, ans_set)
                if board[nx][ny] == "Y":
                    recur(adj + 1, yds, ans_set)
                ans_set.pop()


board = [list(map(str, input().rstrip())) for _ in range(5)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
vis = [[False]*5 for _ in range(5)]
ans_comb = set()
for i in range(5):
    for j in range(5):
        if board[i][j] == 'S':
            recur()
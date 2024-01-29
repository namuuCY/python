def recur(adj, yds, ans_set):
    if adj == 4 and yds == 0 :
        return
    if adj == 5 and yds <= 1:
        return
    if adj == 6 and yds <= 2:
        return
    if adj == 7:
        ans = frozenset(ans_set)                    # 중복되는거 빼내는 방법 중 하나.
        if yds >= 4 and ans not in ans_comb:        # 중복되는걸 계속해서 빼낸다. set활용을 잘하네.
            ans_comb.add(ans)
        return

    for j in range(len(ans_set)):
        x, y = ans_set[j]
        for dir in range(4):
            nx, ny = x+ dx[dir], y+ dy[dir]
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in ans_set and not vis[nx][ny]:
                ans_set.append((nx, ny))                                       # 여기서 vis통해서 한번 간곳 절대 만나는일없음
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
        vis[i][j] = True
        if board[i][j] == 'S':
            recur(1, 1, [(i, j)])
        if board[i][j] == 'Y':
            recur(1, 0, [(i, j)])
            
print(len(ans_comb))
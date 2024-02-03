import sys

N, L = map(int, sys.stdin.readline().split())
road = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
vis = [False] * N   # 경사로가 이미 깔려있는 경우판단위해


# 이렇게 걸러지는 경우가 많을때에는 함수를 통해서 한방에 return 시키는게 편하네

count = 0
is_rotate = False
while True:
    for i in range(N):
        is_possible = True
        vis = [False] * N
        for j in range(N - 1):
            if abs(road[i][j] - road[i][j + 1]) > 1:
                is_possible = False
                break
            if road[i][j] - road[i][j + 1] == 1:
                for tmp in range(j + 1, j + L + 1):
                    if tmp >= N or vis[tmp] or road[i][tmp] != road[i][j+1]:
                        is_possible = False
                        break
                    vis[tmp] = True
            if road[i][j] - road[i][j + 1] == -1:
                for tmp in range(j, j - L, -1):
                    if tmp < 0 or vis[tmp] or road[i][tmp] != road[i][j]:
                        is_possible = False
                        break
                    vis[tmp] = True
            if not is_possible:
                break    
        if is_possible:
            count += 1
    if is_rotate:
        break
    for i in range(N):
        for j in range(i, N):
            road[i][j], road[j][i] = road[j][i], road[i][j] # 대칭시킬때는 범위조심. 이렇게안하면 원래대로
    is_rotate = True        

print(count)



# 한번하고, 회전해서 또할것.



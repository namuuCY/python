import sys

N, L = map(int, sys.stdin.readline().split())
road = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def checking(arr):
    vis = [False] * N       # 매 단위마다 vis를 초기화하면 어떻게해 한줄 전체에서 시작해야지
    for i in range(N - 1):
        if abs(arr[i] - arr[i + 1]) > 1:
            return 0
        if arr[i] - arr[i + 1] == 1:
            for tmp in range(i + 1, i + L + 1):
                if tmp >= N or arr[tmp] != arr[i + 1] or vis[tmp]:
                    return 0
                vis[tmp] = True
        if arr[i] - arr[i + 1] == -1:
            for tmp in range(i, i - L, -1):
                if tmp < 0 or arr[tmp] != arr[i] or vis[tmp]:
                    return 0
                vis[tmp] = True
    else:
        return 1

count = 0    
for x in range(N):
    tmparr = []
    for y in range(N):
        tmparr.append(road[x][y])
    count += checking(tmparr)
    print(x if checking(tmparr)==1 else -1)       # 멍청아 1줄다 보내고 돌려야지
for x in range(N):
    tmparr = []
    for y in range(N):
        tmparr.append(road[y][x])
    count += checking(tmparr)
    print(x if checking(tmparr)==1 else -1)

print(count)
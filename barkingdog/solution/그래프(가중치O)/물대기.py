import sys, heapq

# idea상품) N + 1 개의 정점에서 최소신장트리 구하기로 문제변형

def func(cur):
    global ans
    vis.append(cur)
    for i in range(N + 1):
        if i == cur: continue
        heapq.heappush(edges, (weights[cur][i], cur, i))

    while True:
        w, u, v = heapq.heappop(edges)
        if u in vis and v in vis:
            continue
        break
    ans += w
    if len(vis) != N:
        if u in vis:
            func(v)
        else:
            func(u)
    else:
        return

N = int(input())
cost = []
for i in range(N):
    cost.append(int(input()))
edges = []
weights = []
vis = []
ans = 0

for i in range(N):
    weights.append(list(map(int, sys.stdin.readline().split())))
    weights[i].append(cost[i])
weights.append(cost + [0])

func(0)

print(ans)








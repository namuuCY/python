import sys, heapq

#프림은 임의의 정점 -> 그 정점에 대한 간선을 힙에 넣는다.

N = int(input())
cost = [0 for _ in range(N)]
for i in range(N):
    cost[i] = int(input())
edges = []
weights = []

for _ in range(N):
    weights.append(list(map(int, sys.stdin.readline().split())))

ans = 0
vert = []
# 첫번째는 좀 특별함. 둘다팔지 하나만 팔지에 따라 달라.

def func(cur):
    global ans
    if cur == 0:
        vert.append(cur)
        for i in range(1, N):
            heapq.heappush(edges, (cost[0] + weights[0][i], 0, i))
            heapq.heappush(edges, (cost[i] + weights[0][i], 0, i))
            heapq.heappush(edges, (cost[0] + cost[i], 0, i))
    else:
        for i in range(0, N):
            if i in vert: continue
            heapq.heappush(edges, (weights[cur][i], cur, i))
            heapq.heappush(edges, (cost[i], cur, i))
    while edges:
        weight, u, v = heapq.heappop(edges)
        if u not in vert or v not in vert:
            break
        else: continue
    cost[u], cost[v] = 0, 0
    vert.append(v)
    '''if cur == 0:
        while edges:
            heapq.heappop(edges)
        for j in range(1, N):
            if j == v: continue
            heapq.heappush(edges, (weights[0][i], 0, i))
            heapq.heappush(edges, (cost[i], 0, i))'''

    ans += weight
    print(u, v, weight)
    if len(vert) == N:
        return
    else:
        func(v)
    
func(0)

print(ans)
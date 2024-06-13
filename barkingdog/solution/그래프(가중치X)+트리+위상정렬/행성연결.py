import sys, heapq

# V 1e3개 E 1e6개
# 매번 검색 -> heap -> 프림

N = int(input())

input = sys.stdin.read
data = input().split('\n')

heap = []
adj = []
chk = [False for _ in range(N)]
count = 0
ans = 0

for i in range(N):
    adj.append(list(map(int, data[i].split())))

for i in range(N):
    heapq.heappush(heap, (adj[0][i], 0, i))
chk[0] = True

while count < N - 1:
    while True:
        cost, u, v = heapq.heappop(heap)
        if not chk[v]:
            break
    ans += cost
    count += 1
    chk[v] = True
    for j in range(N):
        if not chk[j]:
            heapq.heappush(heap, (adj[v][j], v, j))
    
print(ans)

        





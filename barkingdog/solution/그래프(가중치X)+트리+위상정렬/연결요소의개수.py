from collections import deque
import sys

N, M = map(int, input().split())

# 고려해야할점. 무방향그래프인지, 인접행렬인지, 인접리스트인지, 초기화방법
# 인접행렬일때는 NxN행렬에서 간선간 값을 adj[u][v]= 1
# 인접그래프일때는 []for _ in range(N)에서 간선에 adj[u].append


def BFS(start):
    Q.append(start)
    vis[start] = True
    while Q:
        cur = Q.popleft()
        for nxt in adj[cur]:
            if vis[nxt]: continue
            Q.append(nxt)
            vis[nxt] = True


Q = deque()
vis = [False] * N

adj = [[] for _ in range(N)]        # 이거 주의 할것. 리스트컴프리헨션으로만!

ans = 0
data = list(map(int, sys.stdin.read().split()))
idx = 0
for _ in range(M):
    fr, to = data[idx], data[idx + 1]
    adj[fr - 1].append(to - 1)
    adj[to - 1].append(fr - 1)
    idx += 2

for i in range(N):
    if vis[i]: continue
    BFS(i)
    ans += 1

print(ans)
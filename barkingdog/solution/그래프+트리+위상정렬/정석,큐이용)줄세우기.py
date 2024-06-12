from collections import deque
import sys

def toplist():
    
    while id0:
        cur = id0.popleft()
        ans.append(cur)
        if not adj[cur]: continue

        for nxt in adj[cur]:
            indeg[nxt] -= 1

            if indeg[nxt] == 0:
                id0.append(nxt)

    return

N, M = map(int, input().split())

adj = [[] for _ in range(N + 1)]
indeg = [0 for _ in range(N + 1)]
id0 = deque()
ans = []
data = list(map(int, sys.stdin.read().split()))

for i in range(0, 2 * M, 2):
    adj[data[i]].append(data[i + 1])
    indeg[data[i + 1]] += 1

for j in range(1, N + 1):
    if indeg[j] != 0: continue
    id0.append(j)

toplist()

print(*ans, sep=' ')






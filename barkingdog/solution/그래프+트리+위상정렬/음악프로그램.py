from collections import deque
import sys

def topsort():

    while id0:
        cur = id0.popleft()
        ans.append(cur)
        if not adj[cur]: continue
        for nxt in adj[cur]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                id0.append(nxt)
        
N, M = map(int, input().split())

raw = list(map(str, sys.stdin.read().split("\n")))
adj = [[] for _ in range(N + 1)]
indeg = [0 for _ in range(N + 1)]
id0 = deque()
ans = []

for i in range(M):
    data = list(map(int, raw[i].split()))
    num = data[0] #비교회수, 즉 간선수는 num-1
    for j in range(1, num):
        adj[data[j]].append(data[j + 1])
        indeg[data[j + 1]] += 1

for k in range(1, N + 1):
    if indeg[k] != 0: continue
    id0.append(k)

topsort()

if len(ans) != N: print(0)
else:
    print(*ans, sep='\n')

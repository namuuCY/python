import sys
from collections import deque

def BFS():
    while Q:
        cur = Q.popleft()
        tr[cur] = True
        for nxt in adj[cur]:
            if tr[nxt]: continue
            Q.append(nxt)

Q = deque()

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
tr = [False for _ in range(N + 1)]

t = sys.stdin.readline().rstrip()
if t == "0":
    print(M)
    exit(0)
else:
    tlist = list(map(int, t.split()))
    for i in range(1, tlist[0] + 1):
        Q.append(tlist[i])
plist = []

for _ in range(M):
    data = list(map(int, sys.stdin.readline().split()))
    pnum = data[0]
    plist.append(data[1:])
    for j in range(1, pnum):
        adj[data[j]].append(data[j + 1])
        adj[data[j + 1]].append(data[j])

BFS()

ans = 0
for k in range(M):
    for p in plist[k]:
        if tr[p]:
            break
    else:
        ans += 1

print(ans)


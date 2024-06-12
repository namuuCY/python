import sys
from collections import deque

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
        tr[tlist[i]] = True

data = list(map(int, sys.stdin.read().split()))
idx = 0
for _ in range(M):
    pnum = data[idx]
    if pnum == 1: 
        idx += 1
        continue
    for i in range(1, pnum):
        adj[data[idx + i]].append(data[idx + i + 1])
        adj[data[idx + i + 1]].append(data[idx + i])
    idx += pnum + 1


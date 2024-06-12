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

for _ in range(M):
    data = list(map(int, sys.stdin.readline().split()))
    pnum = data[0]
    for i in range(1, pnum):
        adj[data[i]].append(data[i + 1])
        adj[data[i + 1]].append(data[i])

    






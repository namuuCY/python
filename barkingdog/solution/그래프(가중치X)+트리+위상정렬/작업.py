import sys
from collections import deque

def func():
    anslist = []
    while id0:
        cur = id0.popleft()
        for nxt in adj[cur]:
            indeg[nxt] -= 1
            
            if indeg[nxt] == 0:




    return max(anslist)


N = int(input())

adj = [[] for _ in range(N + 1)]
timelist = [0 for _ in range(N + 1)] 
anctimelist = [[] for _ in range(N + 1)] # 
indeg = [0 for _ in range(N + 1)]
id0 = deque()
ans = 0

for i in range(1, N + 1):
    data = list(map(int, sys.stdin.readline().split()))
    idx = 0
    timelist[i] = data[idx]
    length = data[idx + 1]
    if length == 0: continue
    
    idx += 2
    for _ in range(length):
        adj[data[idx]].append(i)    #data[idx] 부모 / i 자식
        indeg[i] += 1
        idx += 1

for j in range(1, N + 1):
    if indeg[j] != 0: continue
    id0.append(j)


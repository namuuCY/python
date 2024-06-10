import sys
from collections import deque


def DFS(root):
    Q.append(root)
    P[root] = 0
    while Q:
        cur = Q.pop()
        for nxt in adj[cur]:
            if P[nxt] != -1: continue
            Q.append(nxt)
            P[nxt] = cur


N = int(input())
adj = [[] for _ in range(N)]
Q = deque()
P = [-1 for _ in range(N)]  

data = list(map(int, sys.stdin.read().split()))

for i in range(len(data) // 2):
    adj[data[2 * i] - 1].append(data[2 * i + 1] - 1)
    adj[data[2 * i + 1] - 1].append(data[2 * i] - 1)

DFS(0)
for j in range(N):
    P[j] += 1
print(*P[1:], sep='\n')

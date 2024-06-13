from collections import deque
import sys

def BFS(n):
    Q.append(n)
    vis[n] = True
    while Q:
        cur = Q.popleft()
        for nxt in range(1, N + 1):
            if adj[cur][nxt] == 0: continue
            if vis[nxt]: continue
            Q.append(nxt)
            vis[nxt] = True
            
N  = int(input())
M = int(input())
vis = [False for _ in range(N + 1)]
adj = [[0 for _ in range(N + 1)]]
adj += [([0] + list(map(int, sys.stdin.readline().split()))) for _ in range(N)]

Q = deque()

travel = list(map(int, sys.stdin.readline().split()))

BFS(travel[0])

for i in range(len(travel)):
    if not vis[travel[i]]:
        print("NO")
        exit(0)

print("YES")

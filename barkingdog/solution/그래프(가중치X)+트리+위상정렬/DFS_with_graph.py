from collections import deque

Q = deque()

adj = [[1,2],[2],[3],[0,1,2]]
vis = [False] * 4

def DFS():
    Q.append(0)
    vis[0] = True
    while Q:
        cur = Q.pop()
        print(f"Visited node {cur}")
        for nxt in adj[cur]:
            if vis[nxt]: continue
            Q.append(nxt)
            vis[nxt] = True    

DFS()
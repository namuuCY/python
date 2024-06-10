from collections import deque

Q = deque()

'''adj = [[1,2],[2],[3],[0,1,2]]
vis = [False] * 4
dist = [-1] * 4  # 0번 정점과의 거리
def BFS():
    Q.append(0)
    vis[0] = True
    while Q:
        cur = Q.popleft()
        for nxt in adj[cur]:
            if vis[nxt]: continue
            Q.append(nxt)
            vis[nxt] = True    ''' 

# 모든 간선의 길이가 동일하다면 BFS사용하면됨

adj = [[1,2],[2],[3],[0,1,2]]

dist = [-1] * 4  # 0번 정점과의 거리
def BFS():
    Q.append(0)
    dist[0] = 0
    while Q:
        cur = Q.popleft()
        for nxt in adj[cur]:
            if dist[nxt] != -1: continue
            Q.append(nxt)
            dist[nxt] = dist[cur] + 1

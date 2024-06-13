import sys

class disjointset:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for _ in range(n)]

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        
        if root_u == root_v:
            return False
        
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_u] = root_v
            if self.rank[root_u] == self.rank[root_v]:
                self.rank[root_v] += 1
        return True

input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    travel = disjointset(N + 1)
    edges = []
    count = set()
    ans = 0
    for _ in range(M):
        a, b = map(int, input().split())
        edges.append((a, b))

    for i in range(len(edges)):
        u, v = edges[i]
        if not travel.union(u, v): continue
        ans += 1
        count.add(u)
        count.add(v)
        if len(count) == N:
            break
    print(ans)

        


        

        
    








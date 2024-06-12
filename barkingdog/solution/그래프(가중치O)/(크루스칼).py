import sys

class Disjointset:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for _ in range(n)]
    
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False
        
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_u] = root_v
            if self.rank[root_u] == self.rank[root_v]:
                self.rank[root_v] += 1
        return True
    

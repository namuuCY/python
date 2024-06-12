import sys

n = int(input().rstrip())
m = int(input().rstrip())
INF = 1e9

adj = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
data = list(map(int, sys.stdin.read().split()))

for idx in range(0, 3*m, 3):
    adj[data[idx]][data[idx + 1]] = data[idx + 2]

for i in range(1, n+1):
    print(adj[i])
        

for s in range(1, n + 1):
    adj[s][s] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

for i2 in range(1, n + 1):
    ans = []
    for j2 in range(1, n + 1):
        ans.append(0 if adj[i2][j2] >= INF else adj[i2][j2])
    print(*ans, sep=' ')




    


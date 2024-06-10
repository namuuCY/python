import sys

## 아래와 같이 쓰면 재귀깊이를 설정가능. 단 너무 깊으면 메모리초과남.
sys.setrecursionlimit(10**6)

def DFS(root):
    count = 1
    vis[root] = True
    for nxt in adj[root]:
        if vis[nxt] : continue
        vis[nxt] = True
        count += DFS(nxt)
    countlist[root] = count
    return count

N, R, Q = map(int, input().split())
data = list(map(int, sys.stdin.read().split()))
adj = [[] for _ in range(N)]
vis = [False for _ in range(N)]
ans = []
countlist = [0 for _ in range(N)]

for i in range(0, 2 * (N - 1), 2):
    adj[data[i] - 1].append(data[i + 1] - 1)
    adj[data[i + 1] - 1].append(data[i] - 1)

DFS(R - 1)

for querry in range(2 * (N - 1), len(data)):
    ans.append(countlist[data[querry] - 1])

print(*ans, sep='\n')


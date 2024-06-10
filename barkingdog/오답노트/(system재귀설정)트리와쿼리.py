from collections import deque
import sys


## 아래와 같이 쓰면 재귀깊이를 설정가능. 단 너무 깊으면 메모리초과남.
sys.setrecursionlimit(10**6)


def BFS(root):
    Q.append(root)
    P[root] = root
    
    while Q:
        cur = Q.pop()
        for nxt in adj[cur]:
            if P[nxt] != -1: continue
            Q.append(nxt)
            P[nxt] = cur


def count(cur):
    if countlist[cur] != 0:
        return countlist[cur]
    countlist[cur] = 1
    for nxt in adj[cur]:
        if nxt == P[cur]: continue
        countlist[cur] += count(nxt)
    return countlist[cur]

N, R, Q = map(int, input().split())
data = list(map(int, sys.stdin.read().split()))
adj = [[] for _ in range(N)]
Q = deque()
P = [-1 for _ in range(N)]
ans = []
countlist = [0 for _ in range(N)]

for i in range(0, 2 * (N - 1), 2):
    adj[data[i] - 1].append(data[i + 1] - 1)
    adj[data[i + 1] - 1].append(data[i] - 1)

BFS(R - 1)
count(R - 1)

for querry in range(2 * (N - 1), len(data)):
    ans.append(countlist[data[querry] - 1])

print(*ans, sep='\n')


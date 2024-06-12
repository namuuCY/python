import sys

# 플로이드 알고리즘은 일단 모든 인접행렬을 INF로 초기화
# 매 정보 받을때마다 최솟값을 갱신(가중치가 여러개일수있음.)
# 대각선 값 0으로
# k, i, j순서 기억해야함 반드시 거쳐가는 숫자가 맨 밖에 for문

n = int(input().rstrip())
m = int(input().rstrip())
INF = 1e9

adj = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
data = list(map(int, sys.stdin.read().split()))

for idx in range(0, 3*m, 3):
    adj[data[idx]][data[idx + 1]] = min(adj[data[idx]][data[idx + 1]], data[idx + 2])

for s in range(1, n + 1):
    adj[s][s] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if adj[i][j] < adj[i][k] + adj[k][j]: continue
            adj[i][j] = adj[i][k] + adj[k][j]
            
            # adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

for i2 in range(1, n + 1):
    ans = []
    for j2 in range(1, n + 1):
        ans.append(0 if adj[i2][j2] >= INF else adj[i2][j2])
    print(*ans, sep=' ')




    


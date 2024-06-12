
adj = [[0 for _ in range(10)] for _ in range(10)]

i = 3
j = 4
k = 5
#~~~~ 조건문~~~~
if adj[i][j] < adj[i][k] + adj[k][j]: continue
    adj[i][j] = adj[i][k] + adj[k][j]

# 위가 아래보다 조금 더 빠르다 (상수시간차이)
# 왜냐하면 연산이 대입보다 빠르기 때문.

adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

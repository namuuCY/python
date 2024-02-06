from collections import deque

n = int(input())
Q = deque()
Q.append((1, 0))
vis = [False] * (10**6 + 1)
vis[1] = True
while Q:
    x, s = Q.popleft()
    if x == n:
        print(s)
        exit(0)
    for i in [3 * x, 2 * x,  x + 1]:
        nx = i
        if nx >= 10**6 + 1 or vis[nx]:
            continue
        Q.append((nx, s + 1))
        vis[nx] = True




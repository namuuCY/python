from collections import deque

    # n에서 1로 만드는거보다 1에서 n으로 만드는걸 생각못함.

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




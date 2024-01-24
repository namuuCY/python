
from collections import deque
import sys

n, k = map(int, input().split())
times = [-1] * 100001
Q = deque()
times[n] = 0
Q.append(n)
while Q:
    
    x = Q.popleft()
    
    if x == k:
        print(times[x])
        break
    for nx in { x + 1, x - 1, 2 * x}:
        if nx < 0 or nx >= 100001:
            continue
        if nx == 2 * x:
            if times[nx] == -1 or times[nx] > times[x]:
                times[nx] = times[x]
                Q.append(nx)
            else:
                continue
        if nx == x + 1 or nx == x - 1:
            if times[nx] == -1 or times[nx] > times[x] + 1:
                times[nx] = times[x] + 1
                Q.append(nx)
            else:
                continue
"""
from collections import deque
import sys

n, k = map(int, input().split())
times = [-1] * 100001
Q = deque()
times[n] = 0
Q.append(n)
while Q:
    x = Q.popleft()
    if x == k:
        print(times[x])
        break
    for nx in {x + 1, x - 1, 2 * x}:
        if nx < 0 or nx >= 100001:
            continue
        if nx == x + 1 or nx == x - 1:
            if times[nx] == -1 or times[nx] > times[x] + 1:
                times[nx] = times[x] + 1
                Q.append(nx)
            else:
                continue
        elif nx == 2 * x:
            if times[nx] == -1 or times[nx] > times[x]:
                times[nx] = times[x]
                Q.append(nx)
            else:
                continue """
                
            



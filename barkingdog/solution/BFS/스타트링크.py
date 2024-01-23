from collections import deque
import sys

f, s, g, u, d = list(map(int, sys.stdin.readline().split()))
Q = deque()
button = [-1] * (f)
s -= 1
g -= 1
dir = [u, -d]
Q.append(s)
button[s] = 0
is_possible = False
while Q:
    x = Q.popleft()
    if button[x] == g:
        is_possible = True
        print(button[x])
        break
    for i in dir:
        nx = x + i
        if 0 <= nx < f and button[nx] == -1:
            button[nx] = button[x] + 1
            Q.append(nx)

if not is_possible:
    print('use the stairs')
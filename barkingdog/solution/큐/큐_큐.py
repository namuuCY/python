from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())
data = deque()
for _ in range(n):
    order = list(map(str, sys.stdin.readline().split()))
    if order[0] == 'push':
        data.append(int(order[1]))
    elif order[0] == 'pop':
        if not data:
            print(-1)
        else:
            print(data.popleft())
    elif order[0] == 'size':
        print(len(data))
    elif order[0] == 'empty':
        if len(data) > 0:
            print(0)
        else: print(1)
    elif order[0] == 'front':
        if not data:
            print(-1)
        else:
            tmp = data.popleft()
            print(tmp)
            data.appendleft(tmp)
    elif order[0] == 'back':
        if not data:
            print(-1)
        else:
            tmp = data.pop()
            print(tmp)
            data.append(tmp)
    
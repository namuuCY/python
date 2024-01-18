from collections import deque
import sys

data = deque()

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push_front':
        data.appendleft(int(order[1]))
    elif order[0] == 'push_back':
        data.append(int(order[1]))
    elif order[0] == 'pop_front':
        print(data.popleft() if data else -1)
    elif order[0] == 'pop_back':
        print(data.pop() if data else -1)
    elif order[0] == 'size':
        print(len(data))
    elif order[0] == 'empty':
        print(0 if data else 1)
    elif order[0] == 'front':
        if data:
            tmp = data.popleft()
            print(tmp)
            data.appendleft(tmp)
        else:
            print(-1)
    elif order[0] == 'back':
        if data:
            tmp = data.pop()
            print(tmp)
            data.append(tmp)
        else:
            print(-1)


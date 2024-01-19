from collections import deque
import sys


data = deque()
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    order = sys.stdin.readline().split()
    
    if order[0] == 'push':
        data.append(int(order[1]))

    elif order[0] == 'pop':
        print(data.pop() if data else -1)

    elif order[0] == 'size':
        print(len(data))            # 이거 아무것도안들어갔을땐 0나오는거맞지?

    elif order[0] == 'empty':
        print(0 if data else 1)

    elif order[0] == 'top':
        if data:
            tmp = data.pop()
            print(tmp)
            data.append(tmp)
        else:
            print(-1)

    
    

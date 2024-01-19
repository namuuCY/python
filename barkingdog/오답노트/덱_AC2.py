from collections import deque
import sys, json

tn = int(sys.stdin.readline().rstrip())

for _ in range(tn):
    rcount = 0
    order = str(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    data = deque(json.loads(sys.stdin.readline().rstrip()))
    for i in range(len(order)):
        if order[i] == 'R':
            rcount += 1
        else:
            if data:
                if rcount % 2 == 1:
                    data.pop()
                else:
                    data.popleft()
            else:
                print('error')
                break
    else:                                                           # for 문이 정상적으로(break없이 ) 작동될때만 else가 작동함.
        print('[', end = '')
        print(*list(data) if rcount % 2 == 0 else list(reversed(data)), sep=',', end='')      # 문제점 [1,24,5,6]과 같이 공백없이 리스트를 출력하고싶음
        print(']')

       
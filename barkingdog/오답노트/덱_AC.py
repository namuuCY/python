from collections import deque
import sys, json



tn = int(sys.stdin.readline().rstrip())


def func(a: str):                       # 함수를 새로 정의했더니 이런문제가 생겼다.
    global rcount                       # rcount의 전역변수화 안함.
    if a == 'R':
        rcount += 1
    elif a == 'D':
        if data:
            if rcount % 2 == 1:
                data.pop()
            else:
                data.popleft()
        else:
            print('error')
                                        # error면 아무것도 안떠야 하는데 그거처리못함

for _ in range(tn):
    rcount = 0
    order = str(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    data = deque(json.loads(sys.stdin.readline().rstrip()))
    for i in range(len(order)):
        func(order[i])
    print(list(data) if rcount % 2 == 0 else list(reversed(data)))



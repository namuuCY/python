from collections import deque
import sys

# 입력의 마지막줄에 온점하나. 이걸.... 어떻게


while True:
    string = str(sys.stdin.readline().rstrip())
    if string == '.':
        break
    stk = deque()
    for i in string:
        if i == '(':            # 이거랑
            stk.append(i)
        elif i == '[':          # 이거는 합쳐도 됐다....
            stk.append(i)
        elif i == ')':
            if not stk:
                print('no')     
                break
            elif stk[-1] == '(':
                stk.pop()
            else:
                print('no')
                break
        elif i == ']':
            if not stk:
                print('no')
                break
            elif stk[-1] == '[':
                stk.pop()
            else:
                print('no')
                break
    else:
        print('yes' if not stk else 'no')
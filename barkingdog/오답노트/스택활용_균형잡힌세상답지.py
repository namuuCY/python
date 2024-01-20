from collections import deque
import sys

while True:                                         # 입력의 마지막 . 온점 단 하나의 문장으로 끝내는걸 입력하는 방법임
    string = str(sys.stdin.readline().rstrip())
    if string == '.':
        break
    is_valid = True                         # is_valid라는 bool 표기로 판별을 마지막에 해냄
    stk = deque()
    for i in string:
        if i == '[' or i == '(':
            stk.append(i)
        elif i == ')':
            if not stk or stk[-1] != '(':
                is_valid = False
                break
            stk.pop()
        elif i == ']':
            if not stk or stk[-1] != '[':
                is_valid = False
                break
            stk.pop()
    if stk:                                 # stack이 비었는지 항상 확인해야함. 이거 계속틀린다.
        is_valid = False

    if is_valid:
        print('yes')
    else:
        print('no')
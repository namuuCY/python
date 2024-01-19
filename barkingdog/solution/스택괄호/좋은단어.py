from collections import deque
import sys

n = int(input())

count = 0
for _ in range(n):
    stk = deque()                               # 매번 스택비워야하는데....
    word = str(sys.stdin.readline().rstrip())
    for i in range(len(word)):
        if not stk:
            stk.append(word[i])
        else:
            if word[i] == stk[-1]:
                stk.pop()
            else:
                stk.append(word[i])

    if not stk:
        count += 1
       

print(count)
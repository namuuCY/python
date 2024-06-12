import sys
from collections import deque

sys.setrecursionlimit(10**6)

mstk = deque()
qstk = deque()

N = int(input())
nums = list(map(int, sys.stdin.read().split()))
ans = 0

def c(num):
    global ans
    if not mstk:
        mstk.append(num)
        qstk.append(1)

    else:
        if num < mstk[-1]:
            mstk.append(num)
            qstk.append(1)
            ans += 1
            return
        elif num == mstk[-1]:
            ans += qstk[-1]
            ans += (1 if len(mstk) > 1 else 0)
            qstk[-1] += 1
            return
        else:
            mstk.pop()
            ans += qstk.pop()
            c(num)
            return 
            
            
for num in nums:
    c(num)

print(ans)




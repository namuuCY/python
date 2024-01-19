from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().split()))
stk = deque()
stk.append(2000000)
NGE = []
for i in range(n-1, -1, -1):
    while stk[-1] <= num[i]:
        stk.pop()
    else:
        if stk[-1] > 1000000:
            NGE.append(-1)
        else:
            NGE.append(stk[-1])
        stk.append(num[i])
    
NGE.reverse()
print(*NGE, sep = ' ')
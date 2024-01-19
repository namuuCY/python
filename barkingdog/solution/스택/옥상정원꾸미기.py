from collections import deque
import sys

n = int(input().rstrip())
towers = []
stk = deque()
stk.append((0, 1000000001))
count = []
for _ in range(n):
    towers.append(int(sys.stdin.readline().rstrip()))

towers.reverse()

for i in range(n):
    while stk[-1][1] < towers[i]:
        stk.pop()
    else:
        count.append(i - stk[-1][0])
        stk.append((i + 1, towers[i]))
        
             
print(sum(count))




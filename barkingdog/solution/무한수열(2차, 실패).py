from collections import deque
import sys
n, p, q = map(int, sys.stdin.readline().split())

list = deque()
list.append(n)
ans = 0
while list:
    tmp = list.pop()
    if tmp == 0:
        ans += 1
    else:
        tmpa = tmp // p
        tmpb = tmp // q
        list.append(max(tmpa, tmpb))
        list.append(min(tmpa, tmpb))

print(ans)
    

    


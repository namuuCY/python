from collections import deque
import sys

data = deque()
k = int(sys.stdin.readline().rstrip())

for _ in range(k):
    n = int(sys.stdin.readline().rstrip())
    if n > 0:
        data.append(n)
    elif n == 0:
        data.pop()
    

print(sum(data))
import sys
from collections import deque

N = int(input())
DQ = deque()
data = list(map(int, sys.stdin.readline().split()))
diff = deque()
for i in range(N - 1):
    if data[i + 1] - data[i] != 1 or data[i + 1] - data[i] != 1 - N:
        diff.append(data[i + 1])
    
if data[0] - data[N - 1] != 1 or data[0] - data[N - 1] != 1 - N:
    diff.append(data[0])
len(diff)
if 1 in diff and N in diff:



else:
    


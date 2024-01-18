import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

data = deque(range(1, n+1))

data.rotate(-k)
seq = []
while data:
    seq.append(data.pop())
    data.rotate(-k)

print('<', end='')
for i in range(len(seq)-1):
    print(seq[i], end=', ')
print(f'{seq[len(seq)-1]}' +'>', sep = '', end = '')
import sys

tower = [(100000001, 0)]

n = int(input())
data = list(map(int, sys.stdin.readline().split()))
for i in range(1, n+1):
    length = data[i-1]
    while tower[-1][0] < length:
        tower.pop()
    else:
        print(tower[-1][1], end=' ')
        tower.append((length, i))
import sys

x = []
for _ in range(5):
    y = list(map(int, sys.stdin.readline().split()))
    x.extend(y)

x.sort()

print(sum(x) // 5, x[2] , sep = '\n')
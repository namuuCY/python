import sys

x = list(range(1, 21))

read = sys.stdin.readline
data = [list(map(int, read().split())) for _ in range(10)]

for i in range(10):
    a, b = data[i]
    x[a - 1: b] = reversed(x[a - 1 : b])

print(*x, sep = ' ')
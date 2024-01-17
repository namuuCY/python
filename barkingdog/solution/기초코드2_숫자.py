import sys

a, b = list(map(int, sys.stdin.readline().split()))
if a > b:
    a, b = b, a
x = range(a+1, b)
print(len(x))
print(*x, sep = ' ')
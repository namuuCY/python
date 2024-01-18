import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    print(' ' * i + '*' * (2 * (n - i) - 1))
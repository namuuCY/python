import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    for j in range(i):
        print(' ', end = '')
    for j in range(n-i, 0 , -1):
        print('*', end = '')
    print()
    
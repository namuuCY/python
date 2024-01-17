import sys

dice = sys.stdin.readline
x = list(map(int, dice().split()))

x.sort()

if x[0] == x[2]:
    print(x[0] * 1000 + 10000)
elif x[0] == x[1] or x[0] == x[2]:
    print(x[0 * 100 + 1000])
elif x[1] == x[2]:
    print(x[1] * 100 + 1000)
else:
    print(x[2] * 100)

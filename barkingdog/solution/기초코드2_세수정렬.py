import sys

arr = sys.stdin.readline
data = list(map(int, arr().split()))

data.sort()

print(*data)
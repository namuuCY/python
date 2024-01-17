import sys

n, x = list(map(int, input().split()))

read = sys.stdin.readline
data = list(map(int, read().split()))

m = [k for k in data if k < x]
print(*m)
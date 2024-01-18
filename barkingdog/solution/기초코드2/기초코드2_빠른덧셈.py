import sys

read = sys.stdin.readline

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    a, b = list(map(int,sys.stdin.readline().split()))
    print(a + b)
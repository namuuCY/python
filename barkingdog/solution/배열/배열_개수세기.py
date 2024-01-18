import sys



n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline().rstrip())

print(data.count(x))
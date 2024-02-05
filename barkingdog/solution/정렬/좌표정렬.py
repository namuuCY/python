import sys
N = int(input().rstrip())
dots = []
for _ in range(N):
    dots.append(tuple(map(int, sys.stdin.readline().split())))
dots.sort()
for i in range(N):
    print(*dots[i], sep = ' ')
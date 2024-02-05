import sys
N = int(input().rstrip())
dots = []
for _ in range(N):
    dots.append(list(map(int, sys.stdin.readline().split())))

dots.sort(key=lambda x:(x[1], x[0]))

for i in dots:
    print(*i, sep = ' ')
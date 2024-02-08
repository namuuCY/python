import sys
N = int(input())
times = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
times.sort(key = lambda x: (x[1], x[0]))

curtime = 0
idx = 0
count = 0
for s,e in times:
    if s >= curtime:
        count += 1
        curtime = e
print(count)
    
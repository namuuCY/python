import sys, bisect

N, M = map(int, input().split())

seq = list(map(int, sys.stdin.read().split()))
seq.sort()
ans = 3e9
en = 0
for st in range(N):
    while en < N and seq[en] - seq[st] < M:
        en += 1
    if en == N: break
    ans = min(ans, seq[en] - seq[st])

print(ans)
        

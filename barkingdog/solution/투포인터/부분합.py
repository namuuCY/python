import sys

N, S = map(int, input().split())

seq = list(map(int, sys.stdin.readline().split()))

en = 0
cursum = seq[0]
curlength = 1
ans = 200000
for st in range(N):
    while en < N and cursum < S:
        en += 1
        if en != N:
            cursum += seq[en]
            curlength += 1
    if en == N:
        break
    ans = min(ans, curlength)
    cursum -= seq[st]
    curlength -= 1

print(0 if ans == 200000 else ans)
    
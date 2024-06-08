import sys

def overN(x):
    ans = 0
    for i in range(K):
        ans += (lines[i] // x)
    return ans >= N

K, N = map(int, sys.stdin.readline().split())

lines = list(map(int, sys.stdin.read().split()))

st = 1
en = 2**31 - 1

while st < en:
    mid = (st + en + 1) // 2
    if overN(mid):
        st = mid
    else: 
        en = mid - 1

print(st)
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

    # st, ed값이 1차이 날때를 생각해보고, mid값이 어디에 되어야하는지를 생각해서 +1인지 아닌지 결정.


    if overN(mid):
        st = mid
    else: 
        en = mid - 1

print(st)
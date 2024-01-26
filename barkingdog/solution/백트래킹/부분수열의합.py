import sys

n, s = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

isused = [0] * n
count = 0
ansarr = []
def summation(k: int):
    global count
    if k == n :
        if ansarr and sum(ansarr) == s:
            count += 1
        return
    for i in range(2):
        if i == 1:
            isused[k] = 1
            ansarr.append(seq[k])
            summation(k + 1)
            ansarr.pop()
            isused[k] = 0
        else:
            summation(k + 1)
summation(0)

print(count)
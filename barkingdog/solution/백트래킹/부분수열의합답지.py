import sys
n, m = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

count = 0

def func(cur: int, tot: int):
    global count
    if cur == n:
        if tot == m:
            count += 1
        return
    func(cur + 1, tot + seq[cur])
    func(cur + 1, tot)

func(0, 0)
if m == 0:
    count -= 1
    
print(count)
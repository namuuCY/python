
n, m = map(int, input().split())
data = list(map(str, input().split()))
data.sort()

acount = 0
adata = ['a','e','i','o','u']
bcount = 0
arr = []

def func(k, st):
    global acount
    global bcount
    if k == n:
        if acount >= 1 and bcount >= 2:
            print(''.join(arr))
            return
    for i in range(st, len(data)):
        if data[i] in adata:
            acount += 1
        else:
            bcount += 1
        arr.append(data[i])
        func(k + 1, i + 1)
        arr.pop()
        if data[i] in adata:
            acount -= 1
        else:
            bcount -= 1

func(0, 0)
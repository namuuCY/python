
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
    for i in range(st, len(data)):      # range 안써서 인덱스 오류남..
        if data[i] in adata:
            acount += 1
        else:
            bcount += 1
        arr.append(data[i])             # 이거 원소 추가하는것도 안햇음
        func(k + 1, i + 1)
        arr.pop()
        if data[i] in adata:
            acount -= 1                 # 빼기를 안했음..
        else:
            bcount -= 1

func(0, 0)
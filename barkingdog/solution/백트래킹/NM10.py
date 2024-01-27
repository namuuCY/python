n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
isused = [0] * n 
arr = []

def func(k):
    if k == m:
        print(*arr, sep = ' ')
        return
    tmp = 0
    for i in range(n):
        if isused[i] == 0 and tmp < num[i]:
            for j in range(i + 1):
                isused[j] = 1
            arr.append(num[i])
            tmp = num[i]
            func(k + 1)
            for j in range(i + 1):
                isused[j] = 0
            arr.pop()

func(0)
            
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
isused = [0] * n
arr = []
def func(k):
    tmp = -1  # 마지막 원소 저장
    if k == m:
        print(*arr, sep = ' ')
        return
    for i in range(n):
        if isused[i] == 0 and tmp <= i:
            for j in range(i):
                isused[j] = 1
            tmp = i
            arr.append(numbers[i])
            func(k + 1)
            arr.pop()
            for j in range(i):
                isused[j] = 0
        
func(0)
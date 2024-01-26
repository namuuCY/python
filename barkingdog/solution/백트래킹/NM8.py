n, m = map(int, input().split())
numbers = list(map(int, input().split()))   # 정렬안하고 쓴다고 가정해보자.
numbers.sort()
isused = [0 for _ in range(n)]  
arr = []
def func(idx):
    if idx == m:
        print(*arr, sep = ' ')
        return
    for i in range(n):
        if arr and numbers[i] < arr[-1]:
            continue
        elif not arr:
            arr.append(numbers[i])
            func(idx + 1)
            arr.pop()
        else:                
            arr.append(numbers[i])
            func(idx + 1)
            arr.pop()

func(0)





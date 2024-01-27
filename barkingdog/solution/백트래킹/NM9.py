def func(k, arr, num, isused, n, m):
    if k == m:
        print(' '.join(map(str, arr)))
        return
    tmp = 0
    for i in range(n):
        if not isused[i] and tmp != num[i]: # 파이썬에서 
            isused[i] = True
            arr[k] = num[i]
            tmp = arr[k]
            func(k + 1, arr, num, isused, n, m)
            isused[i] = False

def main():
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    num.sort()
    arr = [0] * m
    isused = [False] * n
    func(0, arr, num, isused, n, m)

if __name__ == "__main__":
    main()
# itertool로 permutation돌리고 set으로 설정한뒤 다시 리스트하면 답 나오긴함

'''
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
isused = [0] * n

def func(idx, arr):
    if idx == m:
        print(*arr, sep = ' ')
        return
    for i in range(n):
        if isused[i] == 1:
            continue
        else:
            isused[i] = 1
            func(idx + 1, arr + [numbers[i]])
            isused[i] = 0

func(0, [])
'''
''' 
n, m = map(int, input().split())        
numbers = list(map(int, input().split()))
numbers.sort()

comb = itertools.permutations(numbers, m)

for i in comb:
    print(*i, sep = ' ')
'''
import itertools

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
isused = [0 for _ in range(n)]

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

''' 아래 방식을 쓰면 같은 9라도 다른 객체로 생각하기 때문에 중복해서 나옴.
n, m = map(int, input().split())        
numbers = list(map(int, input().split()))
numbers.sort()

comb = itertools.permutations(numbers, m)

for i in comb:
    print(*i, sep = ' ')
'''
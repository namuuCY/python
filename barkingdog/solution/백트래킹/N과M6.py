n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()
used = [0 for _ in range(n)]
arr = []
def func(idx):
    if idx == m:
        print(*arr, sep = ' ')
        return

    for i in range(n):
        if used[i] != 1 :
            arr.append(number[i])
            for j in range(i + 1):
                used[j] = 1
            func(idx + 1)
            for j in range(i + 1):
                used[j] = 0
            arr.pop()

func(0)

n, m = map(int, input().split())

ispossible = [True] * (n + 1)
arr = [0 for _ in range(m)]
numbs = list(range(1, n + 1))

def func(idx):
    if idx == m:
        print(*arr, sep = ' ')
        return
    for i in range(1, n+1):
        if ispossible[i]:
            arr[idx] = i
            for k in range(i):
                ispossible[k] = False
            func(idx + 1)
            for k in range(i):
                ispossible[k] = True

func(0)

            


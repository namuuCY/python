n, m = map(int, input().split())

nums = list(range(1, n + 1))

def func(k: int, arr:list):
    if k == n:
        if len(arr) == m:
            print(*arr, sep = ' ')
        return
    func(k + 1, arr +[nums[k]])
    func(k + 1, arr)

func(0, [])

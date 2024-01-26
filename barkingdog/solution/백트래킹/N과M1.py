import sys

n, m = map(int, sys.stdin.readline().split())
arr = [0] * 10
is_used = [False] * 10

def func(k: int):
    if k == m:
        print(*arr[:m], sep = ' ')
        return

    for i in range(1, n + 1):
        if not is_used[i]:
            arr[k] = i
            is_used[i] = True
            func(k + 1)
            is_used[i] = False

func(0)

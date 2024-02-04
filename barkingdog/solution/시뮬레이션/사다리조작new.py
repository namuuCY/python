import sys

N, M, H = map(int, input().split())
ans = 4

dummy = list(range(N))
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    dummy[b - 1], dummy[b] = dummy[b], dummy[b - 1]

def exchange(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]
    return

def recur(n):
    global ans
    if dummy == list(range(N)):
        ans = min(ans, n)
        return
    if n > ans:
        return
    for i in range(N - 1):
        for j in range(i + 1, N):
            exchange(i, j, dummy)
            recur(n + 1)
            exchange(i, j, dummy)

recur(0)
print(ans if ans != 4 else -1)



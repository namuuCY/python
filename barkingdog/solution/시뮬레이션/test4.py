trans = list(map(int, input().split()))
num = list(range(6))
ansarr = []
ans = 9999
def exchange(a, b):
    trans[a], trans[b] = trans[b], trans[a]
    return

def recur(n):
    global ans
    if trans == num:
        if ans > n:
            ans = n
            print(n, ansarr)
        return
    if n > ans:
        return
    if n == 10:
        return
    for i in range(5):
        for j in range(i + 1, 6):
            ansarr.append((i, j))
            exchange(i, j)
            recur(n + 1)
            exchange(i, j)
            ansarr.pop()

recur(0)

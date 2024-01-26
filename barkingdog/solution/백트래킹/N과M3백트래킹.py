import sys

n, m = map(int, input().split())
arr = [0] * m

def pdt(index, n, m):
    if index == m:
        print(*arr, sep = ' ')
        return
    for i in range(1, n + 1):
        arr[index] = i
        pdt(index + 1, n, m)

pdt(0,n,m)

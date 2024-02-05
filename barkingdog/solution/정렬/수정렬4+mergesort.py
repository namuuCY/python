import sys
N = int(input().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
tmp = [0] * N
def merge(st, en):
    mid = (st + en) // 2
    lidx = st
    ridx = mid
    for i in range(st, en):
        if lidx == mid:
            tmp[i] = arr[ridx]
            ridx += 1
        elif ridx == en:
            tmp[i] = arr[lidx]
            lidx += 1
        elif arr[lidx] < arr[ridx]:
            tmp[i] = arr[ridx]
            ridx += 1
        else:
            tmp[i] = arr[lidx]
            lidx += 1        
    for i in range(st, en):
        arr[i]= tmp[i]

def merge_sort(st, en):
    if en == st + 1: return
    mid = (en + st) // 2
    merge_sort(st, mid)
    merge_sort(mid, en)
    merge(st, en)

merge_sort(0, N)
print(*arr, sep = '\n')
    


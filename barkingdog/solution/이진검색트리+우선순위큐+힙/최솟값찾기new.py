import sys, heapq


def getm(cur):
    while heap:
        num, i = heap[0]
        if i <= cur - L:
            heapq.heappop(heap)
            continue
        return num


N, L = map(int, input().split())
seq = list(map(int, sys.stdin.readline().split()))
heap = []
ans = []
if L == 1:
    print(*seq, sep=' ')
else:
    for i in range(N):
        heapq.heappush(heap, (seq[i], i))
        ans.append(getm(i))
    
    print(*ans, sep = ' ')


    
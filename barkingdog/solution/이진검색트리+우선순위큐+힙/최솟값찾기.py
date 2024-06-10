from collections import deque
import heapq, sys

min_heap = []
idx_heap = []

heapq.heapify(min_heap)
heapq.heapify(idx_heap)
counter = {}
ans = []

def get_min():
    while min_heap:
        min_value = heapq.heappop(min_heap)
        if counter[min_value] == 0:
            continue
        heapq.heappush(min_heap, min_value)
        return min_value
    
N, L = map(int, input().split())
seq = list(map(int, sys.stdin.readline().split()))
if L == 1:
    print(*seq, sep=' ')
else:
    for i in range(0, L):
        heapq.heappush(min_heap, seq[i])
        heapq.heappush(idx_heap, (i, seq[i]))
        counter[seq[i]] = counter.get(seq[i], 0) + 1
        ans.append(get_min())
    
    for i in range(L, N):
        heapq.heappush(min_heap, seq[i])
        heapq.heappush(idx_heap, (i, seq[i]))
        counter[seq[i]] = counter.get(seq[i], 0) + 1
        counter[heapq.heappop(idx_heap)[1]] -= 1
        ans.append(get_min())

print(*ans, sep=' ')
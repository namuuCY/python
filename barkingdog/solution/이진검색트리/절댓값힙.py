import sys, heapq


data = sys.stdin.read().split()
heap = []
ans = []

for i in range(1, int(data[0]) + 1):
    num = int(data[i])
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if not heap:
            ans.append(0)
        else:
            ans.append(heapq.heappop(heap)[1])

print(*ans, sep = '\n')
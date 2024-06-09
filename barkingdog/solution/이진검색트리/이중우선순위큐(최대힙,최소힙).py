import heapq, sys
from collections import Counter

class DualQ:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.counter = Counter()
    
    def insert(self, val):
        heapq.heappush(self.min_heap, val)
        heapq.heappush(self.max_heap, -val)
        self.counter[val] += 1

    def delete_min(self):
        while self.min_heap:
            min_value = heapq.heappop(self.min_heap)
            if self.counter[min_value] > 0:
                self.counter[min_value] -= 1
                if self.counter[min_value] == 0:
                    del self.counter[min_value]
                return min_value
        return None
    
    def delete_max(self):
        while self.max_heap:
            max_value = -heapq.heappop(self.max_heap)
            if self.counter[max_value] > 0:
                self.counter[max_value] -= 1
                if self.counter[max_value] == 0:
                    del self.counter[max_value]
                return max_value
        return None
    
    def get_min(self):
        while self.min_heap:
            min_value = self.min_heap[0]
            return min_value
        return None
    
    def get_max(self):
        while self.max_heap:
            max_value = -self.max_heap[0]
            return max_value
        return None
    
    def reset(self):
        self.min_heap.clear()
        self.max_heap.clear()
        self.counter.clear()

    
for _ in range(int(input().rstrip())):
    DQ = DualQ()
    for _ in range(int(input().rstrip())):
        querry, num = sys.stdin.readline().split()
        if querry == 'I':
            DQ.insert(int(num))
        else:
            if num == '1':
                DQ.delete_max()
            else:
                DQ.delete_min()

    if not DQ.min_heap:
        print('EMPTY')
    else:
        print(DQ.get_max(), DQ.get_min())
    
    DQ.reset()
    


        


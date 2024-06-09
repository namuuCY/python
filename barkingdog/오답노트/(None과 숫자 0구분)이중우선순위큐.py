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
        min_value = self.delete_min()
        if min_value is not None:       # 이부분 중요. min_value가 0일경우 False가 된다.
            self.insert(min_value)      # 따라서 None으로 바꿔주는게 중요함.
            return min_value
        return None
    
    def get_max(self):
        max_value = self.delete_max()
        if max_value is not None:
            self.insert(max_value)
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

    if not DQ.counter:
        print('EMPTY')
    else:
        print(DQ.get_max(), DQ.get_min())
    
    DQ.reset()
    


        


import heapq

def heapsort(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h, value)

    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result=heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

def heapsort(iterable):
    i=[]
    result=[]
    for value in iterable:
        heapq.heappush(i, -value)
    for _ in range(len(i)):
        result.append(-heapq.heappop(i))
    return result

result=heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
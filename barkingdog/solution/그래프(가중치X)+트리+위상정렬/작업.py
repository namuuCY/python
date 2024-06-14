import sys
from collections import deque

def func():

    al = []
    while id0:
        cur = id0.popleft()
        acl[cur] += tl[cur]
        al.append(acl[cur])
        for nxt in adj[cur]:
            indeg[nxt] -= 1
            acl[nxt] = max(acl[nxt], tl[cur])
            if indeg[nxt] == 0:
                id0.append(nxt)
    return max(al)


N = int(input())

adj = [[] for _ in range(N + 1)]
tl = [0 for _ in range(N + 1)] 
acl = [0 for _ in range(N + 1)] # 
indeg = [0 for _ in range(N + 1)]
id0 = deque()
ans = 0

for i in range(1, N + 1):   # i 번째 작업
    data = list(map(int, sys.stdin.readline().split()))
    print(data)
    tl[i] = data[0]
    print(f'{i} = {data[0]}')
    for j in range(2, len(data)): #j번째 데이터
        adj[data[j]].append(i)
        print(f'{i}의 조상은 {data[j]}임 {j}번째 인덱스')
        indeg[i] += 1

print(adj)
print(indeg)

    
'''if length == 0: continue
    for _ in range(length):
        adj[data[idx]].append(i)    # i번째 작업의 선행작업(부모)
        indeg[i] += 1
        idx += 1'''

for k in range(1, N + 1):
    if indeg[k] == 0:
        id0.append(k)

print(func())
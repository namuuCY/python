import sys
from collections import deque

# 파싱 후 자료정리: dict두개?
# 자료의 key와 value에 동시에 자유롭게 접근할 자료구조 생각.

def topsort():
    
    while id0:
        cur = id0.popleft()
        for nxt in adj[cur]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                id0.append(nxt)
                clist[cur].append(nxt)
    return
    

N = int(input().rstrip())
names = sys.stdin.readline().split()
names.sort()
numdict = {i:name for i, name in enumerate(names)}
namedict = {name:i for i, name in enumerate(names)}
clist = [[] for _ in range(N)]
adj = [[] for _ in range(N)]
indeg = [0 for _ in range(N)]
id0 = deque()

M = int(input().rstrip())
data = sys.stdin.read().split()
idx = 0

ans = []    # 출력 한꺼번에 잘해봐라

for _ in range(M):
    c, p = data[idx], data[idx + 1]
    adj[namedict[p]].append(namedict[c])
    indeg[namedict[c]] += 1
    idx += 2

for id in range(N):
    if indeg[id] != 0: continue
    id0.append(id)

print(len(id0))
print(' '.join(map(str, [numdict[id0[j]] for j in range(len(id0))])))
topsort()

for k in range(N):
    tmp = [numdict[k], len(clist[k])]
    if len(clist[k]) == 0:
        print(*tmp, sep = ' ')
        continue 
    clist[k].sort()
    for l in clist[k]:
        tmp.append(numdict[l])
    print(*tmp, sep = ' ')    

# 바로출력하는방법?
 


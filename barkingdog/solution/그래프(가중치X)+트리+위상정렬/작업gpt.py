import sys
from collections import deque

def find_max_completion_time(N, times, adj):
    indeg = [0] * (N + 1)
    earliest_start = [0] * (N + 1)
    
    for i in range(1, N + 1):
        for prev in adj[i]:
            indeg[prev] += 1
    
    q = deque()
    for i in range(1, N + 1):
        if indeg[i] == 0:
            q.append(i)
    
    max_time = 0
    while q:
        node = q.popleft()
        current_end_time = earliest_start[node] + times[node]
        max_time = max(max_time, current_end_time)
        
        for next_node in adj[node]:
            indeg[next_node] -= 1
            earliest_start[next_node] = max(earliest_start[next_node], current_end_time)
            if indeg[next_node] == 0:
                q.append(next_node)
    
    return max_time

# 입력 데이터를 직접 설정 (실제 사용시 입력을 받거나 파일에서 읽어야 함)


# 입력 데이터를 처리하는 부분
data = sys.stdin.read().split('\n')
N = int(data[0])
times = [0] * (N + 1)
adj = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    line = list(map(int, data[i].split()))
    times[i] = line[0]
    num_precedents = line[1]
    if num_precedents > 0:
        adj[i].extend(line[2 + num_precedents - 1:])

# 함수를 호출하여 결과를 출력
print(find_max_completion_time(N, times, adj))
from collections import deque
import sys

n, m = map(int, input().split())
Q = deque()
Q.append(n)

dist = [-1] * 100001
dist[n] = 0

while dist[m] == -1:
    x = Q.popleft()
    for i in {x + 1, x - 1, x * 2}:
        if 0 <= i <= 100000 and dist[i] == -1:
            dist[i] = dist[x] + 1
            Q.append(i)         # 다시 넣는거 자꾸 까먹음
print(dist[m])                  # 출력하는것도 자꾸 까먹음




'''
 아래는 내풀이
n, m = map(int, input().split())
if n == m:
    print(0)
    exit(0)
dx = [1, -1, 0]
two = [1, 1, 2]
pq = deque()
time = [-1] * 100001
pq.append(n)
time[n] = 0


while pq:
    x = pq.popleft()
    for i in range(3):
        nx = (x + dx[i]) * two[i]
        if nx == m:
            print(time[x] + 1)
            exit(0)
        if 0 <= nx <= 100000 and time[nx] == -1:
            pq.append(nx)
            time[nx] = time[x] + 1

print(time[m])

'''

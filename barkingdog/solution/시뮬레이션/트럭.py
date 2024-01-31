from collections import deque
import sys

n, w, L = map(int, input().split()) # n 트럭수 w 다리길이 L 최대하중
trucks = deque(list(map(int, sys.stdin.readline().split())))
bridge = deque([0] * w)
times = 0
while trucks:
    times += 1
    if len(bridge) == w:
        bridge.popleft()
    if sum(bridge) + trucks[0] <= L:
        bridge.append(trucks.popleft())
    else:
        bridge.append(0)
times += len(bridge)

print(times)



    


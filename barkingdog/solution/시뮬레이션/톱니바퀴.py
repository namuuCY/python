from collections import deque
import sys
# deque rotate 는 시계 rotate(-1) 은 반시계

gear1 = deque(list(map(int, input().rstrip())))
gear2 = deque(list(map(int, input().rstrip())))
gear3 = deque(list(map(int, input().rstrip())))
gear4 = deque(list(map(int, input().rstrip())))
trial = int(input().rstrip())
for 
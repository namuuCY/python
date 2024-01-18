from collections import deque
import sys

n = int(sys.stdin.readline())
cards = deque(range(1, n+1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(*cards)

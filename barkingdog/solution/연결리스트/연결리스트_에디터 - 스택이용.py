import sys


stk2 = []

word = str(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

stk1 = list(word)

for _ in range(n):
    order = list(map(str, sys.stdin.readline().split()))
    if order[0] == 'L' and stk1:
        stk2.append(stk1.pop())
    elif order[0] == 'D' and stk2:
        stk1.append(stk2.pop())
    elif order[0] == 'B' and stk1:
        stk1.pop()
    elif order[0] == 'P':
        stk1.append(order[1])

stk2.reverse()
ans = stk1 + stk2
print(*ans, sep='')
from collections import deque
import sys

word = str(sys.stdin.readline().rstrip())
ans = 0
stack = deque()
for i in word:
    if i == "(":
        stack.append(i)
    elif i == ")":
        stack.pop()
        ans += len(stack)

print(ans)

    

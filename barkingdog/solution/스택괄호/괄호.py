from collections import deque
import sys

n = int(input())

for _ in range(n):
    is_valid = True
    stack = deque()
    word = str(sys.stdin.readline().rstrip())
    for i in word:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack or stack[-1] !="(":
                is_valid = False
                break
            else:
                stack.pop()
        
    if stack:
        is_valid = False

    print('YES' if is_valid else 'NO')
    



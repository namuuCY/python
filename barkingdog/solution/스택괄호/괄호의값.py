from collections import deque
import sys

word = str(sys.stdin.readline().rstrip())
ans = ""
stack = deque()
temp = deque()
is_valid = True
for i in word:
    if i == '(' or i == '[' :
        if not stack:
            stack.append(i)
            ans = ''.join([ans,'('])
        else:
            stack.append(i)
            ans = ''.join([ans,'+('])
            
    
    elif i == ')':
        if not stack or stack[-1] == '[':
            is_valid = False
            break
        elif stack[-1] == '(':
            temp.append(stack.pop())
            ans = ''.join([ans, '2)'])
        
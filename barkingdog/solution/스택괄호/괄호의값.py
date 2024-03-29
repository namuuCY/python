from collections import deque
import sys, json

word = str(sys.stdin.readline().rstrip())
ans = ""
stack = deque()
is_valid = True
for i in range(len(word)):
    if word[i] == "(" or word[i] == "[" :
        if i > 0 and (word[i - 1] == ")" or word[i - 1] == "]"):
            stack.append(word[i])
            ans = ''.join([ans, ' + '])
        elif not stack:
            stack.append(word[i])
        else:
            stack.append(word[i])
            ans = ''.join([ans, '( '])
    elif word[i] == ")":
        if not stack or stack[-1] != "(" :
            is_valid = False
            break
        else:
            if word[i - 1] == ')' or word[i - 1] == ']' :
                stack.pop()
                ans = ''.join([ans, ' )* 2'])
            else:
                stack.pop()
                ans = ''.join([ans, '2'])
    elif word[i] == "]":
        if not stack or stack[-1] != "[" :
            is_valid = False
            break
        else:
            if word[i - 1] == ')' or word[i - 1] == ']' :
                stack.pop()
                ans = ''.join([ans, ' )* 3'])
            else:
                stack.pop()
                ans = ''.join([ans, '3'])
if not stack:
    is_valid = True

try:
    answer = eval(ans)
except :
    answer = 0

print(answer if is_valid else 0)
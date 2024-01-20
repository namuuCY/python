from collections import deque
import sys

word = str(sys.stdin.readline().rstrip())

stack = deque()
ans = [0] * 20
is_valid = True
for i in range(len(word)):
    if word[i] == "(" or word[i] == "[" :
        stack.append(word[i])
            
    elif word[i] == ")":
        if not stack or stack[-1] != "(" :
            is_valid = False
            break
        else:
            if word[i - 1] == ')' or word[i - 1] == ']' :
                tmp = ans[len(stack) + 1] * 2
                ans[len(stack)] += tmp
                ans[len(stack) + 1] = 0
                stack.pop()
            else:
                ans[len(stack)] += 2
                stack.pop()
                
    elif word[i] == "]":
        if not stack or stack[-1] != "[" :
            is_valid = False
            break
        else:
            if word[i - 1] == ')' or word[i - 1] == ']' :
                tmp = ans[len(stack) + 1] * 3
                ans[len(stack)] += tmp
                ans[len(stack) + 1] = 0
                stack.pop()
            else:
                ans[len(stack)] += 3
                stack.pop()
                
if stack:
    is_valid = False


print(sum(ans) if is_valid else 0)
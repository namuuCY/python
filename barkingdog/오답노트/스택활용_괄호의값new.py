from collections import deque
import sys

word = str(sys.stdin.readline().rstrip())                   # 괄호위치를 스택의 위상, 즉 위아래로 구분함
                                                            # 스택의 길이를 높이로 삼아서 곱하기할때는 아래층으로 내려오는형식으로
stack = deque()
ans = [0] * 20                                              # 맨밑에 주의사항!!!!!!!!!!!!!!
is_valid = True                                             # 맨밑에 주의사항!!!!!!!!!!!!!!
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
                
if stack:                                                   # 내가 원하는거는 비었을때 True
    is_valid = False                                        # not stack 이면 true 쓰지말것. 이건 비었다고 하면 상관없는데   
                                                            # 안비었을 경우 이 구문 통과하게 되고 위에 true값이 그대로 나온다
    

print(sum(ans) if is_valid else 0)
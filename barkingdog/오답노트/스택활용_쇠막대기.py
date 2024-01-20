from collections import deque
import sys

word = str(sys.stdin.readline().rstrip())
ans = 0
stack = deque()
for i in range(len(word)):          # word의 한글자 한글자를 따지려면 글자수의 range만큼이지
    if word[i] == "(":
        if word[i + 1] == "(":
            stack.append(word[i])   # 굳이 스택을 하나 더 만들 생각하지 말고 바로 앞 word의 원소랑 비교할 생각
            ans += 1                
        else:
            stack.append(i)         # 핵심은 레이저가 쪼개지는거 + 판의 개수 두개 생각
    elif word[i] == ")":    
        if word[i - 1] == "(" :
            stack.pop()
            ans += len(stack)
        else:                       # if하고 항상 else생각해줘야함
            stack.pop()

print(ans)
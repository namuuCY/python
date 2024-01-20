from collections import deque
import sys

n = int(input())

count = 0
for _ in range(n):
    stk = deque()                               # 매번 스택비워야하는데....
    word = str(sys.stdin.readline().rstrip())   
    for i in range(len(word)):                  # 처음에는 for i in word라고 했는데 이러면 word 전체로 이해한다
        if not stk:                             # 알파벳단위로 할때는 word[i] 여야함...
            stk.append(word[i])                 # 이거 위에 사실 맞는지 틀린지 확인필요. 테스트필요함.
        else:
            if word[i] == stk[-1]:
                stk.pop()
            else:
                stk.append(word[i])

    if not stk:
        count += 1
       

print(count)
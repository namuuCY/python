from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

nums = deque(range(1, n+1))
stk = deque()
seq = deque()
ansseq = deque()

for _ in range(n):
    ask = int(sys.stdin.readline().rstrip())
    
    while nums and ask >= nums[0]:              # 계속 반복해야할때 while, for 생각
        stk.appendleft(nums.popleft())          
        ansseq.append('+')                      # 맨 마지막 index에서 오류날거같으면
                                                # deque써서 appendleft, popleft로 
                                                # 인덱스 0로 쓰는것도 괜찮음
    if ask == stk[0]:
        seq.append(stk.popleft())
        ansseq.append('-')

    else :
        break

if len(seq) == n:
    print(*ansseq, sep = '\n')
else:
    print('NO')
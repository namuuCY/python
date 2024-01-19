#  L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
#  D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
#  B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
#       삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
#  P $	$라는 문자를 커서 왼쪽에 추가함
#  문제 링크 : https://www.acmicpc.net/problem/1406


import sys


stk2 = []

word = str(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

stk1 = list(word)                           # string은 편집안되니까 list로 바꾸기

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
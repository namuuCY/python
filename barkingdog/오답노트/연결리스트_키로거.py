import sys

stk1 = []
stk2 = []

n = int(sys.stdin.readline().rstrip())

for _ in range(n):

    order = list(map(str, sys.stdin.readline().rstrip()))
    
    for i in range(len(order)):
        if order[i] == '<':                             
            try:
                stk2.append(stk1.pop())             # 비어있는 리스트에서는 pop되지 않음!
            except IndexError:                      # 이 방법도 있지만 비어있지 않은 경우에만 돌아가도록 하는것도 좋음
                pass
        elif order[i] == '>':
            try:
                stk1.append(stk2.pop())
            except IndexError:
                pass
        elif order[i] == '-':
            try:
                stk1.pop()
            except IndexError:
                pass
        else:
            stk1.append(order[i])
    stk2.reverse()                      # 항상 list의 reverse는 따로 만들어줘야함.
    result = stk1 + stk2                
    print(*result, sep='')              
    stk1 = []                           # n번 출력할때마다 초기화 되고, 거기에 새로 써지는지 확인
    stk2 = []


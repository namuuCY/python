import sys

stk1 = []
stk2 = []

n = int(sys.stdin.readline().rstrip())

for _ in range(n):

    order = list(map(str, sys.stdin.readline().rstrip()))
    
    for i in range(len(order)):
        if order[i] == '<':
            try:
                stk2.append(stk1.pop())
            except IndexError:
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
    stk2.reverse()
    result = stk1 + stk2 
    print(*result, sep='')
    stk1 = []
    stk2 = []


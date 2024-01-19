# 창영이는 강산이의 비밀번호를 훔치기 위해서 강산이가 사용하는 컴퓨터에 키로거를 설치했다. 며칠을 기다린 끝에 창영이는 강산이가 비밀번호 창에 입력하는 글자를 얻어냈다.
# 키로거는 사용자가 키보드를 누른 명령을 모두 기록한다. 따라서, 강산이가 비밀번호를 입력할 때, 화살표나 백스페이스를 입력해도 정확한 비밀번호를 알아낼 수 있다. 
# 강산이가 비밀번호 창에서 입력한 키가 주어졌을 때, 강산이의 비밀번호를 알아내는 프로그램을 작성하시오. 강산이는 키보드로 입력한 키는 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표이다.
# 문제 링크 : https://www.acmicpc.net/problem/5397



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


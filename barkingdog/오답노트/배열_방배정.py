import sys
import math                                      # math 모듈의 ceil : 올림함수


data = sys.stdin.readline().rstrip()            # readline 과 readlines가 있음 
people, room = list(map(int, data.split()))           # 전자는 한줄만, 후자는 여러줄 몽땅 읽음
                                                # readline에 ()붙은 readline()은 그때 읽는다는뜻. readline이면 그때그때 한줄씩 읽는거
div = [[0] * 2 for _ in range(6)]

for i in range(people):
    line = sys.stdin.readline().rstrip()
    a,b = map(int, line.split())
    b -= 1
    div[b][a] += 1

for i in range(6):                                      # 내가 만든 행과열, 입력받는 행과 열 반드시 확인하기
    for j in range(2):
        div[i][j] = math.ceil(div[i][j] / room) 

sum = 0

for i in range(6):
    for j in range(2):
        sum += div[i][j] 
print(sum)
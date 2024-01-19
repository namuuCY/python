# 정보 초등학교에서는 단체로 2박 3일 수학여행을 가기로 했다. 여러 학년이 같은 장소로 수학여행을 가려고 하는데 
# 1학년부터 6학년까지 학생들이 묵을 방을 배정해야 한다. 남학생은 남학생끼리, 여학생은 여학생끼리 방을 배정해야 한다. 
# 또한 한 방에는 같은 학년의 학생들을 배정해야 한다. 물론 한 방에 한 명만 배정하는 것도 가능하다.
# 한 방에 배정할 수 있는 최대 인원 수 K가 주어졌을 때, 조건에 맞게 모든 학생을 배정하기 위해 필요한 방의 최소 개수를 구하는 프로그램을 작성하시오.
# 문제 링크 : https://www.acmicpc.net/problem/13300

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
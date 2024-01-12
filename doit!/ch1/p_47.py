import random

n=int(input("난수의 개수?"))

for _ in range(n):
    r= random.randint(10,19)
    print(r, end=' ')
    if r==13:
        print("\n 프로그램을 중단합니다")
        break
else:                               #for 구문에 break 있는거 있을때 좋음
    print("\n 난수 생성 종료")




a=int(input())

for i in range(1, a+1):
    if i*i > a:
        break
    if a%i: continue  #0이 아닌값은 다 1임. 코드돌려 확인해봄 이건똑같네
    print(f"{i}X{a//i}")

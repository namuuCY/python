from max import max_of
import random

t=(4,7,6.6,2,3.14,1)
s='string'
a=['DTS', 'AAC','FLAC']

print(f"이중 최댓값은 {max_of(t)}")
print(f"이중 최댓값은 {max_of(s)}")
print(f"이중 최댓값은 {max_of(a)}")

#---------------------------------------------------------
print('난수의 최댓값')
num=int(input('난수의 개수 몇개?'))
lo= int(input('난수의 최솟값?'))
hi= int(input('난수의 최댓값?'))
x=[None]*num


for i in range(num):
    x[i]=random.randint(lo, hi)     #lo이상 hi이하 난수 생성

print(x)
print(f"이중 최댓값은 {max_of(x)}")


#--------------------------------------------------




print("배열의 최댓값")
print("주의 : 'end' 입력하면 종료")

number=0
x=[]

while True:
    s=input(f"x[{number}]의 값을 입력하세요")
    if s=="end":
        break
    x.append(int(s))
    number+=1

print(f'최댓값은 {max_of(x)}입니다.')

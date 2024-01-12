
n=int(input())
data=list( map(int, input().split()[:n]))     #n개만 입력받는것. :n이면 n-1 값까지만 슬라이스 n:면 이것도 나름 객관적 a:b면 a값, 즉 a+1번째칸부터 b번째칸까지
data.sort()
print(data[1])

def max3(a1,b1,c1):
    maxa=a1
    if b1>maxa: maxa=b1
    if c1>maxa: maxa=c1
    return maxa

print(f"max3(3,2,1)={max3(3,2,1)}")

def mid1(a2,b2,c2):
    if a2>=b2:
        if b2>=c2:
            return b2
        elif a2<=c2:
            return a2
        else:
            return c2
    elif a2>c2:
        return a2
    elif b2>c2:
        return c2
    else:
        return b2

print(mid1(3,6,7))
    




from itertools import combinations_with_replacement 

a=['1','2','3','4']
com1=list(combinations_with_replacement(a,3))
print(com1)
print(len(com1))                                    #len값은 주어진 iterable 객체의 길이수를 보여줌 객체의 한 원소가 tuple이어도 하나로 취급. C랑 다르다


print("이름을 입력 : ", end='')                 # end 넣으면 개행문자 없어지고 ''안에 들어간거 채움
name=input()
print(f"안녕하세요 {name}님?")

print("세 정수의 최댓값?")
a=int(input('정수 a값? : '))   #무조건 input은 문자형이다. 정수형으로 변환이 필요할때 씀
b=int(input('정수 b값? : '))
c=int(input('정수 c값? : '))

maximum=a
if b>maximum: maximum=b
if c>maximum: maximum=c

print(f"최댓값은 {maximum}입니다.") # 글중에 뭐 변수 대입하고싶으면 f집어넣기


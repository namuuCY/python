a=5
b=3
print (a**b)

c=[1,2,3,4,5,6,7,8]     #리스트 자료형이라고 함
print(c)
print(c[4])

d=[]
print(d)

n1=10
e=[0]*n1
print(e)

print(c[-3])            # 끝에서 세번째, 이건 민감 안해도됨
print(c[1:4])           #2~4번째까지 출력.   숫자 민감

arr=[i for i in range(20) if i%2==1]                #range는 1부터 시작한다.
print(arr[-2]) 
arr2=[i*i for i in range(7)]
print(arr2[4])      

arr3=[[0]*a for _ in range(b)]          # 3행 5열의 array 출력 
print(arr3)                             # 그냥 변수없이 반복만을 생각할때는 '_' 언더바를 쓴다고함
                                        # 2차원 리스트 초기화는 무조건 이방법으로 쓰기!
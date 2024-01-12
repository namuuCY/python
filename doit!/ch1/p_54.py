y=[1,2,3]
print(id(y))
y.reverse()
print(y)
print(id(y))                # id함수는 객체가 새로 재할당될때 바뀜. 
                            # 단 list의 원래 형태를 유지하고 여기에 추가하는 append나 reverse, insert 같은건 아닌가봄?


print("왼쪽 아래가 직각인 이등변 삼각형+오른쪽 위가 직각인 이등변 삼각형")
n=int(input("짧은 변의 길이?"))

for i in range(0, n):
    print('*'*(i+1))

for i in range(0,n):
    print(' '*(n-i-1),'*'*(i+1))



n=1
def put_id():                   #id
    x=1
    print(f'id(x)={id(x)}')


print(f'id(1)={id(1)}')
print(f'id(n)={id(n)}')
put_id()
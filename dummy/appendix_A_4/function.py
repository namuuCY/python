def add(a,b):
    return a+b

print(add(3,7))

def add1(a,b):
    print("함수의 결과 : ", a+b)   
add1(4,9)


def add2(a,b):
    print("함수의 결과 : ", a+b)   

add2(b=3, a=2)              # 이런건 좀 융통성있음
print(add(b=7,a=14))        # 융통성 훌륭함

print( (lambda a,b,c:a+b+c)(37,73,10) ) #이건 좀 신기한데


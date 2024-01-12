x=(2,6,3,5,7,1)
#                           tuple은 리버스가 안됩니다. x.reverse()
y=list(reversed(x))        #이건 됨 이건 주어진 iterable 객체를 list로 넘기고 새로 정의하는거라 ㄱㅊ
print(y)

z=[2,6,3,6,7]
z.reverse()
print(z)
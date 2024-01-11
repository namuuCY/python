a=(1,2,3,4)         #튜플이라고함, 순서쌍인듯
print(a)
#a(2)=7              #튜플은 대입으로 초기화가 안된다 오류뜸!

data=dict()
data['사과']='Apple'
data['b사과']='bpple'
data['c사과']='cpple'

if 'b사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다")

key_list=data.keys()                #   사전형 자료 라고함
value_list=data.values()            #구조체느낌이 난다  dict라는 함수가
print(key_list)                     #data라는 이름의 구조체에 keys, values를 요소로 가지고 있고 이 data는 arr형태
print(value_list)

for key in key_list:
    print(data[key])                #key랑 keys랑 확실히 외워둬야할듯?

dat= set([1,1,2,3,4,4,5])           # 집합형 자료, 진짜 집합처럼 겹치는건 뺀다
print(dat)
dat2= {1,1,2,3,4,4,5}
print(dat2)

A=set([1,2,3,4,5])
B={3,4,5,6,7}

print(A|B)          #이건 합집합이니까 | 생각!
print(A&B)          #이건 교집합이니까 & 생각!
print(A-B)          #이건 차집합이니까 - 생각!

dat.add(7)          #집합 관련 함수
print(dat)

dat.update([8,9])
print(dat)

dat.remove(1)
print(dat)

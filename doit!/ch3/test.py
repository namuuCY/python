class Bird:
    def fly(self):
        raise NotImplementedError
    
class Eagle(Bird):
    def fly(self):
        print('super fast')

eagle1=Eagle()
eagle1.fly()



a=[1,2,3,4,5,6,6]
print(a[:2])        # 신기하다 이건 인덱스 2를 포함안하는데
print(a[2:])        # 이건 인덱스 2를 포함함

# 딕셔너리 구성
# dic={(Key1):(Value1),(Key2):(Value2),(Key3):(Value3),(Key4):(Value4),... }
# dic[(Key1)]=(Value1) 이 나옴! 리스트/튜플의 index와 헷갈리지 말것.

# 아래는 예시

b={1:'ㅁ',2:'ㄴ',3:'ㅇ' }
print(b[1])     # 이거 하면 ㅁ 이 출력됨
print(b['ㄴ'])

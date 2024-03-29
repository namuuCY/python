from typing import Any, Sequence        #typing 모듈에서 Any, Sequence라는 타입힌팅(어떤 타입인지 얘기해주는거인듯?)
                                        #Any는 말그대로 아무타입이나 상관x Sequence는 리스트 튜플같은 배열류

def max_of(a:Sequence) -> Any:          
    maximum=a[0]
    for i in range(1,len(a)):
        if a[i]>maximum:
            maximum=a[i]
    return maximum

if __name__=='__main__':                # 이거는 C에서 헤더쓸때 충돌방지하려고 두는거랑 비슷한느낌?
    print('배열의 최댓값')
    num=int(input('원소의 수?'))
    x=[None]*num

    for i in range(num):
        x[i]=int(input(f'x[{i}]의 값을 입력하세요.'))
    
    print(f'최댓값은 {max_of(x)}')
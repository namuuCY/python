from typing import Any, Sequence        #typing 모듈에서 Any, Sequence라는 타입힌팅(어떤 타입인지 얘기해주는거인듯?)
                                        #Any는 말그대로 아무타입이나 상관x Sequence는 리스트 튜플같은 배열류

def max_of(a:Sequence) -> Any:          
    maximum=a[0]
    for i in range(1,len(a)):
        if a[i]>maximum:
            maximum=a[i]
    return maximum

if __name__=='__main__':
    print 
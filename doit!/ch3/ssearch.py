from typing import Any, Sequence

def seq_search(a:Sequence, key:Any) -> int:
    for i in range(len(a)):
        if a[i]==key:
            return i
    return -1

if __name__=='__main__':
    num=int(input('원소 수를 입력하세요: '))
    x=[None]*num
    
    for i in range(num):
        x[i]= int(input(f'x[{i}]:' ))
    
    ky= int(input('검색할 값은? : '))

    idx=seq_searching(x, ky)

    if idx==-1:
        print('검색값을 찾는 원소가 없음')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
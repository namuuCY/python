from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n= len(a)
    for i in range(n//2):
        a[i], a[n-i-1]= a[n-i-1],a[i]

if __name__=='__main__':
    print('배열 순서 역순으로!')
    nx=int(input('원소의 수는?'))
    x=[None]*nx

    for i in range(nx):
        x[i]=int(input(f'x[{i}]의 값을 입력: '))
    
    reverse_array(x)

    print(x)

    
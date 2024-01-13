from typing import Any, Sequence

def bin_search(a:Sequence, key:Any)->int:
    f=0
    l=len(a)-1

    print('  |', end='')
    for i in range(len(a)):
        print(f'{i:4}', end='')
    print()
    print('---+'+(4*len(a)+2)*'-')

    while True:
        pc=(f+l)//2
        print('  |', end='')
        if f!=pc:
            print((f*4+1)*' '+'<-'+((pc-f)*4)*' '+'+',end='')
        else:
            print((pc*4+1)*' '+'<+',end='')
        if pc!=l:
            print(((l-pc)*4-2)*' '+'->')
        else:
            print('->')
        print(f'{pc:2}|', end='')
        for i in range(len(a)):
            print(f'{a[i]:4}', end='')
        print('\n  |')

        if a[pc]==key:
            return pc
        elif a[pc]<key:
            f=pc+1
        else:
            l=pc-1
        if f>l:
            break
    return -1

if __name__=='__main__':
    num=int(input('원소의 수? '))
    x=[None]*num

    print("배열 데이터를 오름차순으로 입력 / 동일한 수는 연속입력 안됨")
    x[0]=int(input('x[0]= '))

    for i in range(1,num):
        while True:
            x[i]=int(input(f'x[{i}]: '))
            if x[i]>=x[i-1]:
                break

    ky=int(input('검색할 값? '))

    idx=bin_search(x,ky)

    if idx==-1:
        print('검색 원소는 존재 않음')
    else:
        print(f'검색값은 x[{idx}]에 있음')

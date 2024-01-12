def conv(x:int, r:int) -> str:
    d=''
    dchar='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    print(f'{r} ) {x}       ')
    print('+----------------')
    
    while True:
        d+=dchar[x%r]
        x//=r
        if x==0:
            break
        print(f'{r} ) {x} -- {x%r}')
        print('+----------------')
    
    return d[::-1]



if __name__=='__main__':
    print("10진수를 n진수로 변환합니다.")

    while True:
        while True:
            no=int(input('음이아닌 정수 입력'))
            if no>=0:
                break
        
        while True :
            cd=int(input('어떤 진수로 변경?'))
            if 2<= cd <=36:
                break
        
        print(f'{cd}진수로는 {conv(no,cd)}입니다.')

        retry =input("한번 더 변환할까요? (Y:예 N:아니오) : ")
        if retry in {'N','n'}:
            break
def gcd(x: int, y: int) -> int:
    
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
    

if __name__=='__main__':
    print('두 정숫값의 최대 공약수.')
    
    x = int(input('첫번째 정수? '))
    y = int(input('두번째 정수? '))

    print(f'최대 공약수는 {gcd(x , y)}입니다. ')
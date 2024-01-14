def fibo(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n >= 3:
        return fibo(n-2)+fibo(n-1)
    else:
        return 0
    
n = int(input('n까지의 피보나치 수열은??'))

for i in range(1, n+1):
    print(f'fibo({i})={fibo(i)}')

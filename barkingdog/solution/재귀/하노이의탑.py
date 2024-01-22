def hanoi(n: int, fp: int, lp: int) -> None:
    if n == 1:
        print(f'{fp} {lp}')
        
    else:
        hanoi(n - 1, fp, 6-fp-lp)
        hanoi(1, fp, lp)
        hanoi(n - 1, 6 - fp - lp, lp )
    
n = int(input())
print(2**n -1)
hanoi(n, 1, 3)

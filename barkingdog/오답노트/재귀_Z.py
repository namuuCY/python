n, r, c = map(int, input().split())


def zfunc(n: int, x: int, y: int) -> int:           # 아이디어는 알았는데
    if n == 0:                                      # 구현을 못했다...
        return 0
    else:
        if x < 2 ** (n-1) and y < 2 ** (n-1):
            return zfunc(n-1, x, y)
        elif x < 2 ** (n-1) and 2 ** (n-1) <= y < 2 ** (n):
            return zfunc(n-1 , x, y - 2 ** (n-1)) + 2 ** (2*n - 2)
        elif y < 2 ** (n-1) and 2 ** (n-1) <= x < 2 ** (n):
            return zfunc(n-1 , x- 2 ** (n-1), y ) + 2 * (2 ** (2*n - 2))
        elif 2 ** (n-1) <= x < 2 ** (n) and 2 ** (n-1) <= y < 2 ** (n):
            return zfunc(n-1 , x- 2 ** (n-1), y - 2 ** (n-1)) + 3 * (2 ** (2*n - 2))
        

print(zfunc(n, r, c))
        
    




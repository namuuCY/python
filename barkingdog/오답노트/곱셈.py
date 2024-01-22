def func(p: int, q: int, r: int) -> int:
    if q == 0:                   # 무식하지만 속도는 빨랐죠? 존나빨랐죠?
        return 1
    elif q == 1:
        return p % r
    elif q == 2:
        return p ** 2 % r
    elif q == 3:
        return p ** 3 % r
    elif q == 4:
        return p ** 4 % r
    elif q == 5:
        return p ** 5 % r
    elif q == 6:
        return p ** 6 % r
    elif q == 7:
        return p ** 7 % r
    elif q == 8:
        return p ** 8 % r
    elif q == 9:
        return p ** 9 % r
    else:
        return (func(p, q // 10, r)** 10) * func(p, q % 10, r) % r
    
a, b, c = list(map(int, input().split()))
print(func(a, b, c))


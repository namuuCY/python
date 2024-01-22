def func(a: int, b: int, c: int) -> int:
    if b == 1:
        return a % c
    elif b % 2 == 0:
        val = func(a, b//2, c)
        return val * val % c
    else:
        val = func(a, b//2, c)
        return val * val * a % c
    
a, b, c = list(map(int, input().split()))
print(func(a, b, c))


# 밑의 함수는 재귀함수 안에 재귀함수를 두번 불러서 시간복잡도가 너무 길어지는 결과 초래함
# 재귀함수 안에 재귀함수가 두번이상 들어갈경우 시간복잡도가 logn 이 아니라 n 이 되는 결과 초래함
"""
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

"""
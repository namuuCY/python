import sys

a, b, c = list(map(int, input().split()))

if a == b and b == c :
    print(a * 1000 + 10000)
elif a == b or a == c :
    print(a * 100 + 1000 )
elif b == c:
    print(b * 100 + 1000)
else:
    print(max(a,b,c) * 100)



import sys, math

n = int(input().rstrip())

for _ in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))
    cd = math.gcd(a,b)
    print(a * b // cd)




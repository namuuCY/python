import sys, math

n = int(input())
data = [] * n
data = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    cd = math.gcd(data[0], data[i])
    print(f"{data[0] // cd}/{data[i] // cd}")
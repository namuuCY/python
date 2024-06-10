import sys

def pow(a,n):
    if n == 1:
        return a
    else:
        sq = pow(a, n // 2)
        if n % 2 == 0:
            return (sq * sq) % 1000000007
        else:
            return (sq * sq * a) % 1000000007
        
def modinv(a):
    return pow(a, 1000000005)



M = int(input())

data = list(map(int, sys.stdin.read().split()))

ans = 0

for i in range(0, 2 * M, 2):
    ans += data[i + 1] * modinv(data[i])
    ans %= 1000000007

print(ans)


    
    
pow
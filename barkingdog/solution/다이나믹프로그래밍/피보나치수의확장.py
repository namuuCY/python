n = int(input())
DP = {}
DP[0] = 0
DP[1] = 1
DP[-1] = 1

# 계산해보니까 -짝수일때 -의 항, -홀수일때 양수의 항이랑 똑같음.

if abs(n) > 1:
    for i in range(2, abs(n) + 1):
        DP[i] = (DP[i - 1] + DP[i - 2]) % 1000000000
        DP[-i] = DP[i]

if n == 0:
    print(0)
    print(DP[0])
elif n > 0 or n % 2 == 1:
    print(1)
    print(DP[n])
else:
    print(-1)
    print(DP[n])
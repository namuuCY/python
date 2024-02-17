from math import sqrt

N = int(input())
DP = {}
for i in range(1, round(sqrt((10 ** 5) + 1)) + 1):
    DP[i * i] = 1
    DP[2 * i * i] = 2

if N >= 3:
    for i in range(3, N + 1):
        if i in DP:
            continue
        else:
            DP[i] = min(DP[j] + DP[i - j] for j in range(1, (i+1 //2)))

print(DP[N])

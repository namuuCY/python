from math import sqrt

N = int(input())
DP = {0:0, 1:1}

for i in range(2, N + 1):
    DP[i] = min((DP[i - (j * j)] + 1) for j in range(1, int(sqrt(i) + 1)))  # int는 버림, round는 반올림, ceil은 올림

print(DP[N])

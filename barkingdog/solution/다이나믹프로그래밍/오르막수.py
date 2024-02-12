DP = {}
for i in range(10):
    DP[(1, i)] = 1
N = int(input())

if N >= 2:
    for i in range(2, N + 1):
        for j in range(0, 10):
            DP[(i, j)] = sum(DP[(i - 1, k)] for k in range(j + 1)) % 10007

print(sum(DP[N, i] for i in range(10)) % 10007)

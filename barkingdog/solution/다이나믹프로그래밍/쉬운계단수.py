N = int(input())

DP = [[0 for _ in range(10)] for _ in range(N)]
DP[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(1, N):
    DP[i][0] = DP[i - 1][1]
    DP[i][9] = DP[i - 1][8]
    for j in range(1, 9):
        DP[i][j] = (DP[i - 1][j - 1] + DP[i - 1][j + 1]) % 1000000000

print(sum(DP[N-1]) % 1000000000)
        
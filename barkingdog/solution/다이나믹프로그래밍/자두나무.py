import sys
T, W = map(int, input().split())
fall = [0] + list(map(int, sys.stdin.read().split()))
DP = [[0 for _ in range(W + 1)] for _ in range(T + 1)]  # i번째 떨어질때 
for i in range(1, T + 1):                                      # j번째 이동했을때 최대
    for j in range(min(i, W) + 1):
        if fall[i] % 2 == 1:
            if j == 0:
                DP[i][j] = DP[i - 1][j] + 1
            elif j % 2 == 0:
                DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j]) + 1
            else:
                DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j])
        if fall[i] % 2 == 0:
            if j == 0:
                DP[i][j] = DP[i - 1][j]
            elif j % 2 == 1:
                DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j]) + 1
            else:
                DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j])

print(max(DP[T]))

DP = {1:1, 2:2, 3:4}
trial = int(input())
for i in range(4, 1000001):
    DP[i] = (DP[i-1] + DP[i - 2] + DP[i - 3]) % 1000000009
for _ in range(trial):
    print(DP[int(input())])


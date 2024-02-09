# 1 1 1 2 2 3 4 5 7 9 12 16
# 1 2 3 4 5 6 7 8 9 10 11 12

DP = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(11, 101):
    DP.append(DP[i - 1] + DP[i - 5])    # 

trial = int(input())
for _ in range(trial):
    print(DP[int(input())])
import sys
# 동전의 최소개수 출력
n, k = map(int, input().split())
coins = list(map(int, sys.stdin.read().split()))
coins.sort()
DP = [-1] * (k + 1)
DP[0] = 0

for i in range(1, k + 1):
    ans = []
    for j in range(0, n):
        if i - coins[j] < 0:
            break
        if DP[i - coins[j]] == -1:
            continue
        ans.append(DP[i - coins[j]])
    if ans:
        DP[i] = min(ans) + 1

print(DP[k])






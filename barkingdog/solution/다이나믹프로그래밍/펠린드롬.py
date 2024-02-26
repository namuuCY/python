import sys

N = int(input())
nums = [0] + list(map(int, sys.stdin.readline().split()))
DP = {}
for i in range(1, N + 1):
    DP[(i, i)] = 1
for i in range(1, N):
    if nums[i] == nums[i + 1]:
        DP[(i, i + 1)] = 1
    else:
        DP[(i, i + 1)] = 0

for gap in range(2, N):
    for i in range(1, N - gap + 1):
        if DP[(i + 1, i + gap - 1)] == 1 and nums[i] == nums[i + gap]:
            DP[(i, i + gap)] = 1
        else:
            DP[(i, i + gap)] = 0
ans = []
for _ in range(int(input())):       # 한줄씩 출력하는것보다 한줄씩 답에 추가한뒤 한꺼번에 출력이빠름.
    i, j = map(int, sys.stdin.readline().split())
    ans.append(DP[(i, j)])
print(*ans, sep = '\n')






# 아래의 방법은 1,5가 형성되기 전에 2,4 가 형성되어있어야하는데 그렇게 되지 못해서 틀림
'''DP = [[0] * (N + 1) for _ in range(N + 1)]      
for i in range(1, N + 1):
    for j in range(i, N + 1):
        if j - i == 0:
            DP[i][j] = 1
        elif j - 1 == 1:
            if nums[i] == nums[j]:
                DP[i][j] = 1
            else:
                DP[i][j] = 0
        else:
            if DP[i + 1][j - 1] == 1:
                if nums[i] == nums[j]:
                    DP[i][j] = 1
                else:
                    DP[i][j] = 0
            else:
                DP[i][j] = 0

for _ in range(int(input())):
    i, j = map(int, sys.stdin.readline().split())
    print(DP[i][j])
'''



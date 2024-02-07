import sys

# n번째 계단을 밟을 수 있는 경우의 수
D = {}  # n일때 마지막 스텝이 +2
E = {}  # n일때 마지막 스텝이 +1

n = int(input().rstrip())
stair = [0] + list(map(int, sys.stdin.read().split()))

while len(stair) < 310:
    stair.append(0)
D[1] = 0
E[1] = stair[1]
D[2] = stair[2]
E[2] = stair[1] + stair[2]
D[3] = stair[1] + stair[3]
E[3] = stair[2] + stair[3]

if n >= 4:
    for i in range(4, n + 1):
        D[i] = max(D[i - 2] + stair[i], E[i - 2] + stair[i])
        E[i] = D[i - 1] + stair[i]

ans = max(D[n], E[n])       # n = 1일때 D[1]값이 정의되지 않아서 틀림

print(ans)
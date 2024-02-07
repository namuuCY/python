import sys

N, M = map(int, input().split())
nums = list(map(int, sys.stdin.readline().split()))
D = {}
D[1] = sum(nums)
for i in range(2, N + 2):
    D[i] = D[i - 1] - nums[i - 2]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(D[i] - D[j + 1])
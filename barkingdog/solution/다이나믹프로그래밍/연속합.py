import sys

n = int(input())
nums = [0] + list(map(int, sys.stdin.readline().split()))

D = {0:0}
for i in range(1, n + 1):
    D[i] = max(0, D[i - 1]) + nums[i]

del D[0]
print(max(D.values()))

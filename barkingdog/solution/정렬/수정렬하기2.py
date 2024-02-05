import sys

N = int(input().rstrip())
nums = [0] * 10001
for i in range(N):
    nums[int(sys.stdin.readline().rstrip())] += 1
for i in range(10001):
    for j in range(nums[i]):
        print(i, sep = '\n')
    

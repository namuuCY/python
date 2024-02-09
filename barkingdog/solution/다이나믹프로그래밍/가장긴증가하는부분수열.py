import sys
N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
DP = [0] * 1001 # nums[i]를 끝으로 하는 가장 긴 증가하는 부분수열의 길이
for i in range(N):
    DP[nums[i]] = max(DP[:nums[i]]) + 1

print(max(DP))

    

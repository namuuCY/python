import sys

#super 빠른방법
input()
print('\n'.join(map(str,sorted(map(int, sys.stdin.readlines())))))

'''
N = int(input().rstrip())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))
nums.sort()
ans = map(str, nums)
print('\n'.join(ans))
'''


# 아래가 counting sort방법
'''  
import sys

N = int(input().rstrip())
nums = [0] * 2000001

for _ in range(N):
    nums[int(sys.stdin.readline().rstrip()) + 1000000] += 1

for i in range(2000001):
    for j in range(nums[i]):
        print(i - 1000000)
맞긴한데 시간이 너무 오바됨
'''
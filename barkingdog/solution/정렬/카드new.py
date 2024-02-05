import sys
N = int(input().rstrip())
nums = list(map(int, sys.stdin.readlines()))
nums.sort()
nums.append(2**62 + 1)
ans = nums[0]
count = 1
mxcount = 1

for i in range(N):
    if nums[i] == nums[i + 1]:
        count += 1
    else:
        if mxcount < count:
            ans = nums[i]
            mxcount = count
        count = 1
print(ans)
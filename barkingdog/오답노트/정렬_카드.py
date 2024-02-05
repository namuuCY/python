import sys
N = int(input().rstrip())
nums = list(map(int, sys.stdin.readlines()))
nums.sort()
ans = nums[0]
maxcount = 0
count = 0
for i in range(0, N - 1):
    if nums[i] == nums[i + 1]:
        count += 1
    else:
        if maxcount < count:    # 이렇게 될경우 마지막수에대한 처리가없음.
            maxcount = count
            ans = nums[i]
        count = 0
if count > maxcount:            # 그래서 예외구문추가하는거
    ans = nums[N - 1]
print(ans)
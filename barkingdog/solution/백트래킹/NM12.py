n, m = map(int, input().split())
nums = list(set(map(int, input().split())))
nums.sort()
n = len(nums)
arr = []
def func(k, st):
    if k == m:
        print(' '.join(map(str, arr)))
        return
    idx = 0
    for i in range(st, n):
        if i >= idx:
            arr.append(nums[i])
            idx = i         # 같은자리에 같은 숫자 이상으로만 나오게 하기 위한것.
            func(k + 1, i)
            arr.pop()

func(0, 0)
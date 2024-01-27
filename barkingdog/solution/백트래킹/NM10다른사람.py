n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = []

def seq(k, st):     # k는 수열의 길이, st는 이전값보다 크게하는 지점
    if k == m:
        print(*arr, sep = ' ')
        return
    tmp = 0
    for i in range(st, n):
        if tmp != nums[i]:
            arr.append(nums[i])
            tmp = nums[i]
            seq(k + 1, i + 1)
            arr.pop()
            
seq(0, 0)

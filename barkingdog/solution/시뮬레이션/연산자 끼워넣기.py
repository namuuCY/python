N = int(input().rstrip())
nums = list(map(int, input().split()))
cals = list(map(int, input().split())) #덧,뺄,곱,나
maxans = -1e9
minans = 1e9

def div(a, b):
    if a < 0:
        return -((-a) // b)
    else: a // b

def recur(n, ans):
    global maxans, minans
    if n == N - 1:
        maxans = max(maxans, ans)
        minans = min(minans, ans)
        return
    for i in range(4):
        if cals[i] == 0:
            continue
        if i == 0:
            cals[i] -= 1
            recur(n + 1, ans + nums[n + 1])
            cals[i] += 1
        elif i == 1:
            cals[i] -= 1
            recur(n + 1, ans - nums[n + 1])
            cals[i] += 1
        elif i == 2:
            cals[i] -= 1
            recur(n + 1, ans * nums[n + 1])
            cals[i] += 1
        elif i == 3:
            cals[i] -= 1
            recur(n + 1, div(ans, nums[n + 1]))
            cals[i] += 1

recur(0, nums[0])
print(maxans)
print(minans)
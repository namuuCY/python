N = int(input().rstrip())
nums = list(map(int, input().split()))
cals = list(map(int, input().split())) #덧,뺄,곱,나
maxans = -1e9       # 10억이 딱 나오는 경우에는 값이 10억.0이 나옴
minans = 1e9        # 아래에 쓴게 정답

def div(a:int, b:int):
    if a < 0:
        return -((-a) // b)
    else: 
        return a // b       

def recur(n, ans):
    global maxans, minans
    if n == N - 1:
        maxans = max(maxans, ans)
        minans = min(minans, ans)
        return
    for i in range(4):
        if cals[i] == 0:
            continue
        cals[i] -= 1
        if i == 0:
            recur(n + 1, ans + nums[n + 1])
        elif i == 1:
            recur(n + 1, ans - nums[n + 1])
        elif i == 2:
            recur(n + 1, ans * nums[n + 1])
        elif i == 3:
            recur(n + 1, div(ans, nums[n + 1]))
        cals[i] += 1

recur(0, nums[0])
print(maxans)
print(minans)

'''
N = int(input().rstrip())
nums = list(map(int, input().split()))
cals = list(map(int, input().split())) #덧,뺄,곱,나
maxans = 0
minans = 0
is_first = True
def div(a:int, b:int):
    if a < 0:
        return -((-a) // b)
    else: 
        return a // b       # return을 안써넣어서

def recur(n, ans):
    global maxans, minans, is_first
    if n == N - 1:
        if is_first:
            maxans = ans
            minans = ans
            is_first = False
            return
        else:
            maxans = max(maxans, ans)
            minans = min(minans, ans)
            return
    for i in range(4):
        if cals[i] == 0:
            continue
        cals[i] -= 1
        if i == 0:
            recur(n + 1, ans + nums[n + 1])
        elif i == 1:
            recur(n + 1, ans - nums[n + 1])
        elif i == 2:
            recur(n + 1, ans * nums[n + 1])
        elif i == 3:
            recur(n + 1, div(ans, nums[n + 1]))
        cals[i] += 1

recur(0, nums[0])
print(maxans)
print(minans)'''
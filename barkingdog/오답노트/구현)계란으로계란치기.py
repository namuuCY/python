import sys

ans = 0
count = 0

def breaker(idx):        # idx는 들고있는 계란의 index
    global ans
    global count
    if idx == n:
        ans = max(ans, count)
        return
    if eggs[idx][0] <= 0 or count == n - 1:
        breaker(idx + 1)
        return
    for i in range(0, n):
        if i != idx and eggs[i][0] > 0:
            eggs[idx][0] -= eggs[i][1]
            eggs[i][0] -= eggs[idx][1]
            if eggs[idx][0] <= 0: count += 1
            if eggs[i][0] <= 0: count += 1
            breaker(idx + 1)
            if eggs[idx][0] <= 0: count -= 1
            if eggs[i][0] <= 0: count -= 1
            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]

n = int(input().rstrip())   # [][0]이 내구도 [][1]이 무게
eggs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

breaker(0)
print(ans)
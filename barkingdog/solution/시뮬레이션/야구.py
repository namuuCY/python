import sys
from collections import deque


N = int(input())

hit = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

isused = [False for _ in range(9)]
ans = 0
order = [0 for _ in range(9)]
def run(): # 1이닝 통틀어서
    global ans
    idx = 0
    score = 0

    for inn in range(N):
        outcount = 0
        running = [False for _ in range(4)]            
        while outcount < 3:
            r = hit[inn][order[idx]]
            if r == 4:
                score += 1 + running.count(True)
                running = [False for _ in range(4)]            
            elif 1<= r < 4:
                n_running = [False for _ in range(4)]
                for i in range(3, 0, -1):
                    if running[i]:
                        if i + r > 3:
                            score += 1
                        else:
                            n_running[i + r] = True
                n_running[r] = True
                running = n_running
            else:
                outcount += 1
            idx += 1
            idx %= 9
    ans = max(ans, score)

def brute(k):
    if k == 9:
        run()
        return
    
    if k == 3:
        order[3] = 0
        isused[0] = True
        brute(k + 1)
        return

    for i in range(1, 9):
        if isused[i]: continue
        isused[i] = True
        order[k] = i
        brute(k + 1)
        isused[i] = False

brute(0)

print(ans)
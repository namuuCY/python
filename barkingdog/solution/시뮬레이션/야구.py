import sys
from collections import deque

sys.setrecursionlimit(10**6)

N = int(input())

hit = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

isused = [False for _ in range(9)]
running = deque()
ans = 0
order = []
def run(): # 1이닝 통틀어서
    global ans
    idx = 0
    score = 0

    for inn in range(N):
        outcount = 0
        while running:
            running.pop()

        while outcount < 3:
            r = hit[inn][order[idx % 9]]
            if r == 4:
                while running:
                    running.pop()
                    score += 1
                score += 1
            elif r > 0:
                for i in range(len(running)):
                    if running[i] + r >= 4:
                        running.popleft()
                        score += 1
                    else: running[i] += r
                running.append(r)
            else:
                outcount += 1
            idx += 1
    ans = max(ans, score)

def brute(k):
    if k == 9:
        run()
        return
    
    if k == 3:
        isused[k] = True
        order.append(k)
        brute(k + 1)
    
    for i in range(9):
        if isused[i]: continue
        isused[i] = True
        order.append(i)
        brute(k + 1)
        order.pop()
        isused[i] = False

brute(0)

print(ans)
from itertools import permutations
from collections import deque
import sys

def scoremachine(stat, runner):
    global score, outcount, hitteridx
    if stat == 0:
        outcount += 1
        hitteridx += 1
        return
    elif stat == 4:
        score += sum(runner) + 1
        runner = [0] * 3
        hitteridx += 1
        return
    else:
        for idx in range(3 - stat, 3):
            if runner[idx]:
                score += 1
                runner[idx] = 0
        for idx in range(0, 3 - stat):
            runner[idx + stat] = 1
            runner[idx] = 0
        runner[stat - 1] = 1
        hitteridx += 1    
        return

inning = int(input())
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(inning)] 

comb = permutations(range(1,9), 8)

ans = 0

for c in comb:
    hitteridx = 0
    score = 0
    players = list(c)
    players.insert(3, 0)
    for i in range(inning):
        runner = [0] * 3
        outcount = 0
        while True:
            if outcount == 3:
                break
            scoremachine(stat[i][players[hitteridx % 9]], runner)
        if outcount == 3:
            continue
    ans = max(score, ans)    
print(ans)
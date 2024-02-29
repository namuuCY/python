import sys
from datetime import datetime

n = int(input())
flower = [[0] * 2 for _ in range(n)]
for i in range(n):
    a1, a2, b1, b2 = map(int, sys.stdin.readline().split())
    flower[i][0] = a1 * 100 + a2
    flower[i][1] = b1 * 100 + b2
flower.sort(key = lambda x: (-x[1], x[0]))
print(*flower, sep = '\n')
def choose(sd, flower):
    for i in range(n):
        if flower[i][0] <= sd:
            return flower[i][1]
    else:
        print(0)
        exit(0)

ans = 0
next = choose(301, flower)
ans += 1
for _ in range(365):
    tmp = choose(next, flower)      # 무한루프
    if tmp == next:
        print(0)
        break
    if tmp >= 1130:
        ans += 1
        print(ans)
        break
    ans += 1
    next = tmp










    

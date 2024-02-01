import sys
from itertools import combinations

n, m = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken.append((i, j))
        if board[i][j] == 1:
            house.append((i, j))
                                    # 당연히 치킨집이 많을수록 치킨거리는 줄어드는건데 바로 m때렸어야함
'''def abs(a, b):
    return a - b if a > b else b - a'''

def dist(x1, y1, x2, y2):       # 이거 절댓값 함수 없나?
    return abs(x1 - x2) + abs(y1 - y2)

case = list(combinations(chicken, m))

sumlist = []
for c in case:
    sumdist = 0
    for h in range(len(house)):
        x1, y1 = house[h]
        distlist = 200
        for i in range(len(c)):
            x2, y2 = c[i]
            distlist = min(distlist, dist(x1, y1, x2, y2))
        sumdist += distlist
    sumlist.append(sumdist)

print(min(sumlist))

        




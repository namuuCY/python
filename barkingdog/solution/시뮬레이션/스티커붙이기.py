import sys
from copy import deepcopy

n, m, k = map(int, sys.stdin.readline().split())
note = [[0] * m for _ in range(n)]

def rot():
    global r, c, sticker
    tmp = deepcopy(sticker)               # 2차원 배열은 deepcopy사용해야함.
    new_sticker = [[0] * r for _ in range(c)]
    for i in range(c):
        for j in range(r):
            new_sticker[i][j] = tmp[r- 1 - j][i]
    r, c = c, r
    sticker = new_sticker
    return

def rot2(sticker):
    global r, c
    new_sticker = [list(row) for row in zip(*sticker[::-1])]
    sticker = new_sticker
    r, c = c, r
    return

def pastable(x, y):
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1 and note[x + i][y + j] == 1:  # 인덱스 주의
                return False
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                note[x + i][y + j] = 1
    return True

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    sticker = [ list(map(int, sys.stdin.readline().split())) for _ in range(r)]

    for _ in range(4):
        is_paste = False
        for x in range(n - r + 1): 
            if is_paste: break
            for y in range(m - c + 1):
                if pastable(x, y):
                    is_paste = True
                    break
        if is_paste: break
        rot2(sticker)

ans = 0
for i in range(n):
    for j in range(m):
        ans += note[i][j]
print(ans)

        

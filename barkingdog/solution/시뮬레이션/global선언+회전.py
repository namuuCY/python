from copy import deepcopy

# 스티커를 아예 새로운 객체(리스트)로 할당하는 경우에, list 또한 global 선언을 해줘야함
# list의 어떤 값을 바꾸는 경우에는 객체가 달라지는게 아니지만 아예 새로 선언하는거는 객체가 달라지는거라 반드시 해줘야함.

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

def rot2():
    global r, c, sticker                    
    new_sticker = [list(row) for row in zip(*sticker[::-1])]
    sticker = new_sticker
    r, c = c, r
    return


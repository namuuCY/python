from collections import deque
import sys
# deque rotate 는 시계 rotate(-1) 은 반시계
gear = []
for _ in range(4):
    gear.append(deque(list(map(int, input().rstrip())))) 
trial = int(input().rstrip())
for _ in range(trial):
    rotation = [0] * 4
    number, rotnum = map(int, input().split())
    is_rotate = [False] * 3
    for i in range(3):
        is_rotate[i] = (gear[i][2] != gear[i + 1][6])
    if number == 1:
        rotation[0] = rotnum
        rotation[1] = (-1) * is_rotate[0] * rotation[0]
        rotation[2] = (-1) * is_rotate[1] * rotation[1]
        rotation[3] = (-1) * is_rotate[2] * rotation[2]
    elif number == 2:
        rotation[1] = rotnum
        rotation[0] = (-1) * is_rotate[0] * rotation[1]
        rotation[2] = (-1) * is_rotate[1] * rotation[1]
        rotation[3] = (-1) * is_rotate[2] * rotation[2]
    elif number == 3:
        rotation[2] = rotnum
        rotation[1] = (-1) * is_rotate[1] * rotation[2]
        rotation[3] = (-1) * is_rotate[2] * rotation[2]
        rotation[0] = (-1) * is_rotate[0] * rotation[1]
    elif number == 4:
        rotation[3] = rotnum
        rotation[2] = (-1) * is_rotate[2] * rotation[3]
        rotation[1] = (-1) * is_rotate[1] * rotation[2]
        rotation[0] = (-1) * is_rotate[0] * rotation[1]
    for r in range(4):
        gear[r].rotate(rotation[r])

print(gear[0][0] * 1 + gear[1][0] * 2 + gear[2][0] * 4 + gear[3][0] * 8)


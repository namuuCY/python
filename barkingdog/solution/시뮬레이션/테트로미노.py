from copy import deepcopy
import sys

N, M = map(int, input().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def rotate(arr, i):
    if i == 1:
        return [list(row) for row in zip(*arr[::-1])]
    if i == 2:
        return rotate(rotate(arr, 1), 1)
    if i == 3:
        return rotate(rotate(arr, 2), 1)

tet = {}
tet[0] = [[1, 1], [1, 1]]
tet[1] = [[1, 1, 1, 1]]     # 0,4,5 번은 1번, 2,3,6번은 3번돌려야함
tet[2] = rotate(tet[1], 1)
tet[3] = [[1, 0], [1, 1], [0, 1]]
tet[4] = rotate(tet[3], 1)
tet[5] = [[0, 1], [1, 1], [1, 0]]
tet[6] = rotate(tet[5], 1)
tet[7] = [[1, 0], [1, 0], [1, 1]]
tet[11] = [[0, 1], [0, 1], [1, 1]]
tet[15] = [[1, 1, 1], [0, 1, 0]]
for i in range(1,4):
    tet[7 + i] = rotate(tet[7], i)
    tet[11 + i] = rotate(tet[11], i)
    tet[15 + i] = rotate(tet[15], i)

def tetadd(x, y, arr):
    sum = 0 
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                sum += board[x + i][y + j]
    return sum
ans = 0
for num in range(19):
    r, c = len(tet[num]), len(tet[num][0])
    for x in range(N - r + 1):
        for y in range(M - c + 1):
            ans = max(ans, tetadd(x, y, tet[num]))

print(ans)



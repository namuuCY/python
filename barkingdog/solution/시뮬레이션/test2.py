def rot(arr, dir):
    global board
    if dir == 0:
        return
    elif dir == 1:
        for i in range(5):
            for j in range(5):
                arr[i][j] = arr[4 - j][i]
        return
    elif dir == 2:
        for i in range(5):
            for j in range(5):
                arr[i][j] = arr[4 - i][4 - j]
        return
    else:
        for i in range(5):
            for j in range(5):
                arr[i][j] = arr[j][4 - i]
        return

board= [[1,1,1,1,1],[1,0,0,0,1], [1,0,0,0,1], [1,0,0,0,0], [1,0,0,0,0] ]
rot(board, 1)
print(*board, sep ='\n', end = '\n')
print()
rot(board, 3)
print(*board, sep ='\n', end = '\n')
print()
rot(board, 2)
print(*board, sep ='\n', end = '\n')
print()
rot(board, 2)
print(*board, sep ='\n', end = '\n')
print()
rot(board, 3)
print(*board, sep ='\n', end = '\n')
print()
rot(board, 1)
print(*board, sep ='\n', end = '\n')
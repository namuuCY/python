order = {}

order[3] = 123
order[7] = 67667

print(order)

if 3 in order:
    print(order[3])
else:
    print('X')


def rotate(arr, i):
    if i == 1:
        return [list(row) for row in zip(*arr[::-1])]
    if i == 2:
        return rotate(rotate(arr, 1), 1)
    if i == 3:
        return rotate(rotate(arr, 2), 1)
tet = {}
tet[0] = [[1, 1], [1, 1]]
tet[1] = [[1, 1, 1, 1]]  

tet[2] = rotate(tet[1], 1)
print(*tet[2], sep = '\n')

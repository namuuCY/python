from collections import deque
import sys

n = int(input().rstrip())
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
Q = deque()

def bfs(x: int, y: int) -> int:
    area = 1
    Q.append((x, y))
    while Q:
        x, y = Q.popleft()
        for k in range(4):          # range 값은 4지 이사람아
            nx, ny = x + d[k][0], y + d[k][1]
            if 0 <= nx < n and 0 <= ny < n and town[nx][ny] == '1':
                area += 1
                town[nx][ny] = '0'
                Q.append((nx, ny))
    return area

town = [list(sys.stdin.readline().rstrip()) for _ in range(n)]          # 리스트화 시키긴 했는데 하나의 변수가 str이었네
arr = []
for i in range(n):
    for j in range(n):
        if town[i][j] == '1':
            town[i][j] = '0'
            arr.append(bfs(i, j))


print(len(arr))
arr.sort()
print(*arr, sep = '\n')


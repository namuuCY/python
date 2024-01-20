import sys

n = int(input())

for _ in range(n):
    M, N, x, y = list(map(int, sys.stdin.readline().split()))
    is_right = False
    for i in range(N):
        if (i * M + x ) % N == (y % N):
            print(i * M + x)
            is_right = True
            break
    if not is_right:
        print(-1)
        



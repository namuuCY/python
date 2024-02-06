import sys
Trial = int(input())

for _ in range(Trial):
    count = 0
    N, M = map(int, input().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    A.sort(reverse=True)
    B.sort()
    idx = M - 1
    is_end = False
    for i in range(N):
        if A[i] > B[idx]:
            count += (idx + 1)
        else:
            while A[i] <= B[idx]:
                if idx == -1:
                    is_end = True
                    break
                idx -= 1
            count += (idx + 1)
        if is_end:
            break
    print(count)



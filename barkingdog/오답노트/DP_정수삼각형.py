import sys

n = int(input())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
D = []
D.append([nums[0][0]])
if n >= 2:
    for i in range(1, n):
        tmp = []
        for j in range(i + 1):      # i + 1 인덱스 틀림
            if j == 0:
                tmp.append(D[i - 1][0] + nums[i][j])
            elif j == i:                    # j == i 도 인덱스 틀림
                tmp.append(D[i - 1][-1] + nums[i][j])
            else:
                tmp.append(max(D[i - 1][j - 1], D[i - 1][j]) + nums[i][j])
        D.append(tmp)
print(max(D[n - 1]))

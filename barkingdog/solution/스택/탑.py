from collections import deque
import sys


topstk = deque()        # 0은 인덱스, 1은 탑길이

n = int(sys.stdin.readline().rstrip())
ans = [0] * n
toplen = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    while topstk:
        tmp = topstk.pop()
        if tmp[1] > toplen[i]:
            ans[i] = tmp[0]
            topstk.append(tmp)
            topstk.append([i + 1, toplen[i]])
            break
        else:
            continue

    else:
        ans[i] = 0
        topstk.append([i + 1, toplen[i]])

print(*ans, sep = ' ')

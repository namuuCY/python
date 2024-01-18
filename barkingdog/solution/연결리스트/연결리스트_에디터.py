from collections import deque
import sys

word = sys.stdin.readline().rstrip()
ans = deque(word)

idx = len(ans)

n = int(sys.stdin.readline().rstrip())

for i in range(n):

    flist = list(map(str, sys.stdin.readline().split()))

    if flist[0] == 'L':
        if idx > 0:
            idx -= 1

    elif flist[0] == 'D':
        if idx < len(ans):
            idx += 1

    elif flist[0] == 'B':
        if idx > 0:
            del ans[idx - 1]
            idx -= 1

    elif flist[0] == 'P':
        if idx == len(ans):
            ans.append(flist[1])
            idx += 1
        else:
            ans.insert(idx, flist[1])
            idx += 1

print(*list(ans), sep='')


import sys
N = int(input())
seq = list(map(int, sys.stdin.readline().split()))

DP = {(seq[0], 1):[seq[0]]}
for num in seq:
    tmp = []
    tmplen = 0
    for last, length in DP:
        if last < num:
            if length + 1 > tmplen:
                tmp = DP[(last, length)] + [num]
                tmplen = length + 1
    if not tmp:
        DP[(num, 1)] = [num]
    else:
        DP[(num, tmplen)] = tmp

ans = list(DP.values())
ans.sort(key=lambda x: -len(x))
print(len(ans[0]))
print(*ans[0], sep = ' ')
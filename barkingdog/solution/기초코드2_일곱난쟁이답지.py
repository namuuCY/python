import sys

nan = []
result = []
for i in range(9):
    a = int(sys.stdin.readline())
    nan.append(a)

for i in range(8):
    for j in range(i + 1,9):
        result = []
        for k in range(9):
            if k != i and k != j:
                result.append(nan[k])
        if sum(result) == 100:
            break
    if sum(result) == 100:
        break
result.sort()
print(*result, sep = '\n')




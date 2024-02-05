import sys

N = int(input().rstrip())
data = []
for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    data.append([int(age), name])

def compare(arr):
    return arr[0]

data.sort(key=compare)

# 혹은 data.sort(key=lambda x: x[0])로도 설정가능!

for i in range(N):
    print(*data[i], sep = ' ')


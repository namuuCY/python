import sys

N = int(input().rstrip())
data = []
for _ in range(N):
    data.append(list(sys.stdin.readline().rstrip()))

def std1(arr):
    sum = 0
    for i in range(len(arr)):
        if '0' <= arr[i] <= '9':
            sum += int(arr[i])
    return sum

data.sort(key= lambda x: (len(x), std1(x), x))

for gui in data:
    print(''.join(gui))

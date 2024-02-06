import sys

data = set()

N = int(input())
for _ in range(N):
    data.add(sys.stdin.readline().rstrip())

arr = list(data)

arr.sort(key = lambda x: (len(x), x))

print('\n'.join(arr))
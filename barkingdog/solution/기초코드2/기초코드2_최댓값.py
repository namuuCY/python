import sys

data = []
for _ in range(9):
    a = int(sys.stdin.readline().rstrip())
    data.append(a)

num = max(data)
idx = data.index(num)

print(num, idx + 1, sep='\n')
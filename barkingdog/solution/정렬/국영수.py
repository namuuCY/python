import sys

N = int(input())
data = []
for i in range(N):
    name, n1, n2, n3 = map(str, sys.stdin.readline().split())
    data.append([name] + list(map(int, [n1, n2, n3])))     # map은 iterator다

sorted_data = sorted(data, key = lambda x: (-x[1], x[2], -x[3], x[0]))

print('\n'.join([sorted_data[i][0] for i in range(N)]))

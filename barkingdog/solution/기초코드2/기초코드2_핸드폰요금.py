import sys

n = int(input())
data = list(map(int, sys.stdin.readline().split()[:n]))

sum1 = 0
sum2 = 0

for i in data:
    sum1 += ((i // 30) + 1) * 10

for i in data:
    sum2 += ((i // 60) + 1) * 15

if sum1 > sum2:
    print('M', sum2, sep=' ')
elif sum1 < sum2:
    print('Y', sum1, sep=' ')
else:
    print('Y', 'M', sum1, sep=' ')
import sys

x = [] 
for i in range(7):
    y = int(input())
    if y % 2 == 1:
        x.append(y)

x.sort()

if sum(x) == 0:
    print(-1)
else:
    print(sum(x), x[0], sep='\n')
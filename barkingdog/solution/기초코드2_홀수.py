import sys

x = [] 
for i in range(7):
    y = int(input())
    if y % 2 == 1:
        x.append(y)

x.sort()
print(sum(x), x[0], sep='\n')
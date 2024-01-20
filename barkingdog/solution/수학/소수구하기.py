import sys

m, n = list(map(int, sys.stdin.readline().split()))
ans = []

if m % 2 == 0 and n % 2 == 0:
    if m == 2:
        ans.append(2)
    for i in range(m + 1, n + 1, 2):
        while 


elif m % 2 == 1 and n % 2 == 0:

elif m % 2 == 0 and n % 2 == 1:

else: #m % 2 == 1 and n % 2 == 1

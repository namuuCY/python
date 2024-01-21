import math, sys

a, b = list(map(int, sys.stdin.readline().split()))

A = math.ceil(math.sqrt(a))
B = int(math.sqrt(b))
count = 0
print(A,B)
if A <= 2:
    count += 1
pns = []
num = max(3, A)

if A % 2 == 0:
    for i in range(A + 1, B + 1, 2):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            pns.append(i)
            count += 1
else:
    for i in range(A , B + 1, 2):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            pns.append(i)
            count += 1

for i in range(len(pns)):
    for j in range():


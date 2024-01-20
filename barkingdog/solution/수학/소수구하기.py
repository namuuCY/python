import sys, math

m, n = list(map(int, sys.stdin.readline().split()))
ans = []

if m <= 2:
    ans.append(2)

num = max(3, m)

if num % 2 == 0:
    for i in range(num + 1, n + 1, 2):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            ans.append(i)

else:
    for i in range(num, n + 1, 2):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            ans.append(i)

print(*ans, sep = '\n')
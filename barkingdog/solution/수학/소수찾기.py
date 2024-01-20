import sys, math

n = int(input().rstrip())

data = list(map(int, sys.stdin.readline().split()))
count = 0
for i in data:
    if i == 1:
        continue
    elif i == 2:
        count += 1
        continue
    else:
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
                    
print(count)            

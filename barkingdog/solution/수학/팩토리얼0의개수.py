import math

n = int(input())

count = 0

def fivdiv(n: int) -> int:
    div = 0
    while n > 4 and n % 5 == 0:
        div += 1
        n //= 5
    return div

for i in range(n+1):
    if i % 5 == 0:
        count += fivdiv(i)
       
print(count)

    


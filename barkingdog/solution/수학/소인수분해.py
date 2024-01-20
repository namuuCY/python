import sys

n = int(input())

while n != 1:
    for i in range(2, 100000000):       # 2로 나눈다는걸 왜 생각을못하지..
        if n % i == 0:
            print(i)
            n //= i
            break


    
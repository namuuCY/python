a=int(input("직사각형의 넓이는?"))

import math


for i in range(1, round(math.sqrt(a+1)+1)):
    if a%i==0:
        print(f"{i}X{a//i}")



print("1부터 n까지의 정수의 합은?")

while True:
    n=int(input())
    if n>0:
        break

sum=0
for i in range(1,n+1):
    sum+=i

print(sum)

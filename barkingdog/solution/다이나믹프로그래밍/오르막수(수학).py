# 0~9 까지 중복해서 10개 뽑는 경우의수 칸막이 9개 물건 n개
from math import factorial

n = int(input())
ans = (factorial(n + 9) // (factorial(n) * factorial(9))) % 10007

print(ans)
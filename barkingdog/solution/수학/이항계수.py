import sys
import math

a,b = list(map(int, sys.stdin.readline().split()))

ans = (math.factorial(a) // (math.factorial(b) * math.factorial(a-b))) % 10007

print(ans)
import sys
from enum import Enum


arr = "DCBAE"
for i in range(3):
    x = list(map(int, sys.stdin.readline().split()))
    y = sum(x)
    print(arr[y])
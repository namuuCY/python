import sys
from typing import MutableSequence

def reverse(x: MutableSequence, a: int, b: int) -> None:
    a -= 1
    b -= 1
    for i in range(a, (a + b) // 2 + 1):
        x[i], x[a + b - i] = x[a + b - i], x[i]
    
 
read = sys.stdin.readline
x = list(range(1, 21))
matrix = [list(map(int, read().split())) for _ in range(10)]

for i in range(10):
    reverse(x, matrix[i][0], matrix[i][1])

print(*x, sep = ' ')
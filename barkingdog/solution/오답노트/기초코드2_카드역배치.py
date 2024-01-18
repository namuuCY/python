import sys
from typing import MutableSequence

def reverse(x: MutableSequence, a: int, b: int) -> None:
    a -= 1                                                  # 이거 연산 미리해두고 하는게 편하긴함
    b -= 1                                                  
    for i in range(a, (a + b) // 2 + 1):                    # 나누기 2할때와 range에서 주의해야할게
        x[i], x[a + b - i] = x[a + b - i], x[i]             # 나누기 2하면 1과 8 사이에서 중앙값이 a+b //2 면 4가나옴. 근데 range라 4번째 인덱스는 포함X
                                                            # 따라서 중앙값을   (a+b+1) // 2    로 하는게 좋다 
    
 
read = sys.stdin.readline
x = list(range(1, 21))
matrix = [list(map(int, read().split())) for _ in range(10)]

for i in range(10):
    reverse(x, matrix[i][0], matrix[i][1])

print(*x, sep = ' ')
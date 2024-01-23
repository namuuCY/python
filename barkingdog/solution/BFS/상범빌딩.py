from collections import deque
import sys

dir = [[1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1]]

while True:                                             # 입력값이 너무 ㅈ같은경우!
    L, R, C = map(int, sys.stdin.readline().split())
    if L == 0 and R == 0 and C == 0:
        break
    maze = []
    Q = deque()

    for _ in range(L):
        layer = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
        sys.stdin.readline()            # 빈줄 읽어넘기기
    
    


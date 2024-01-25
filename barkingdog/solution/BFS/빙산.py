from collections import deque
import sys

# 빙산 1년 후 높이 함수 / 높이 최댓값함수 /  그점기준 1덩어리인지 bfs 후 그이상있는지 확인 + bfs함수

n, m = map(int, input().split())
ice = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def melt() -> tuple:
    for i in range(n):
        for j in range(m):
            if ice[i][j] == 0:
                for dir in range(4):
                    ni, nj = i+dx[dir], j+dy[dir]
                    if ice[ni][nj] != 0:
                        ice[ni][nj] -= 1


    




        
        
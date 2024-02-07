import sys
#2차원테이블을 정의하는 거 생각하기
N = int(input())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
D = []
D.append([cost[0][0], cost[0][1], cost[0][2]])

for i in range(1, N):
    D.append([min(D[i - 1][1], D[i - 1][2])+ cost[i][0], 
              min(D[i - 1][0], D[i - 1][2])+ cost[i][1], 
              min(D[i - 1][0], D[i - 1][1])+ cost[i][2]])

print(min(D[N - 1]))

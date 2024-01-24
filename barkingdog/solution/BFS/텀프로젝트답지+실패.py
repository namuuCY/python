from collections import deque
import sys
# 자기 자신을 계속해서 순환시키면 언젠가는 자기자신으로 돌아오는 애들이 있음
# 걔들을 카운트하는 방식으로 하는 첫번째 방법 (시간복잡도 n제곱

# 이 문제의 포인트는  "움직이면서 사이클에 포함된 애들인가 / 사이클에 포함되지 못한애들인가의 정보를 남기는것"
# 그 방면에서 BFS와 방식이 동일하다.

CYCLE_IN = -1
NOT_VISITED = 0

def run(x: int) -> None:
    cur = x
    while True:
        state[cur] = x
        cur = arr[cur]
        if state[cur] == x:
            while state[cur] != CYCLE_IN:
                state[cur] = CYCLE_IN
                cur = arr[cur]
            return
        elif state[cur] != NOT_VISITED:
            return



trial = int(input().rstrip())
for _ in range(trial):
    count = 0
    n = int(input().rstrip())
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    state = [NOT_VISITED] * (n + 1)

    for i in range(1, n + 1):
        if state[i] == NOT_VISITED:
            run(i)
        
    for j in range(1, n + 1):
        if state[j] != CYCLE_IN:
            count += 1
        
    print(count)







'''
trial = int(input().rstrip())
for _ in range(trial):
    n = int(input().rstrip())
    wantteam = list(map(int, sys.stdin.readline().split()))     # 이거 입력값들이 다 +1 씩 되어있음 인덱스 주의
    team = [1] * n      # 팀 이뤘으면 0, 아직 팀 없으면 1
    Q = deque()
    for i in range(n):
        if wantteam[i] == i + 1:
            team[i] = 0
        elif wantteam[i] != i + 1 and team[i] == 1 :
            Q.append(i)         # i+1 번째 사람
            while Q:
                tmp = wantteam[Q[-1]] - 1       # i+1번째 사람이 원하는 사람
                if tmp == Q[0]:
                    while Q:
                        team[Q.pop()] = 0
                if team[tmp] == 0:
                    Q.clear()                   # 덱은 클리어가 가능
                    break
                if team[tmp] == 1:
                    Q.append(tmp) 
    print(sum(team))
'''

    



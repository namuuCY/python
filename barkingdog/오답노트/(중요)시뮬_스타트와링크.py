from itertools import combinations
import sys
# https://www.acmicpc.net/source/71946537
# 특이한 풀이인데 이해가 안감. 참고.
# 팀 조합은 최대 18만가지, 그중에 합하는과정 최대 90가지*2 가지치기필요함.

N = int(input().rstrip())
stats = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
members = list(range(N))
combi = combinations(members, N//2)     

# itertools는 이터레이터를 반환하고 값을 반환X
'''for comb in combi:                      
    print(comb) '''

'''first_combi = next(combi, None) 과 같이 접근. 여기서 None은 없을경우 None을 반환하라는뜻'''
# 와 같이 한번에 하나씩 접근해야함. 어떤 특정 인덱스값에 접근할경우 에러남.
ans = 10000
for comb in combi:
    statone = 0
    stattwo = 0
    notcomb = [i for i in range(N) if i not in comb]
    for i, j in list(combinations(comb, 2)):
        statone += stats[i][j] + stats[j][i]
    for i, j in list(combinations(notcomb, 2)):
        stattwo += stats[i][j] + stats[j][i]           # 이미 i,j 둘다 바꿔서 나올수있는 구조라 i,j j,i둘다더할필요X
    gap = abs(statone-stattwo)
    if gap == 0:
        print(0)
        exit(0)
    ans = min(ans, gap)
print(ans)

    

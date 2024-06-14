import sys

seqdict = {}

# 수열 전체의 길이에서 최장 연속 부분수열의 길이를 빼면된다.

# list 사용해도될듯...?

N = int(input())
num = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    seqdict[num[i]] = seqdict.get(num[i] - 1, 0) + 1

print(N - max(seqdict.values()))

    




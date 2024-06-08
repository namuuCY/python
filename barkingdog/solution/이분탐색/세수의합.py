from itertools import combinations_with_replacement
import sys
N = int(input())

numlist = list(map(int, sys.stdin.read().split()))
numlist.sort()
twosumlist = set()
combs = combinations_with_replacement(numlist, 2)

for comb in combs:
    twosumlist.add(sum(comb))


for i in range(N-1, 0, -1):
    for j in range(i):
        if (numlist[i] - numlist[j]) in twosumlist:

            print(numlist[i])
            exit(0)





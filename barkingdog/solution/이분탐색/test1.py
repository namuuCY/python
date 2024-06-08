import sys

input()

numlist = list(map(int, sys.stdin.readline().split()))
sortednums = list(set(numlist))
sortednums.sort()
cardlist = {}

for i in range(len(sortednums)):
    cardlist[sortednums[i]] = i

answer = []

for num in numlist:
    answer.append(cardlist.get(num))
print(*answer, sep=' ')
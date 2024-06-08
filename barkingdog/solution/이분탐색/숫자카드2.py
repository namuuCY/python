import sys

input()

numdict = {}
for num in map(int, sys.stdin.readline().split()):
    val = numdict.get(num, 0)
    numdict[num] = val + 1

input()

for ans in map(int, sys.stdin.readline().split()):
    print(numdict.get(ans, 0))

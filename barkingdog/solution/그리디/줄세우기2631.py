import sys

N = int(input())

seqdict = {}

for i in map(int, sys.stdin.read().split()):
    if not seqdict:
        seqdict[i] = 1
        continue
    tmp = []
    for key in seqdict:
        if key < i:
            tmp.append(seqdict[key])
    seqdict[i] = max(tmp) + 1 if tmp else 1

print(N - max(seqdict.values()))
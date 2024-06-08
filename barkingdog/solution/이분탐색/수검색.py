import sys

def BinSearch(target):
    st = 0
    ed = N - 1
    while st <= ed:
        mid = (st + ed + 1) // 2
        if NumberList[mid] == target:
            Answer.append(1)
            return
        elif NumberList[mid] < target:
            st = mid + 1
        else:
            ed = mid - 1
    Answer.append(0)
    return

N = int(input().rstrip())
NumberList = list(map(int, sys.stdin.readline().split()))
NumberList.sort()

M = int(input().rstrip())
TargetList = list(map(int, sys.stdin.readline().split()))

Answer = []

for target in TargetList:
    if NumberList[0] == target or NumberList[N - 1] == target:
        Answer.append(1)
        continue
    BinSearch(target)

print(*Answer, sep='\n')
    


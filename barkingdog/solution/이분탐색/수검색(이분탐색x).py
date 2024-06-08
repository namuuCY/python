import sys

input()
numlist = set(map(int, sys.stdin.readline().split()))
input()
for number in map(int, sys.stdin.readline().split()):
    if number in numlist:
        print(1)
    else:
        print(0)
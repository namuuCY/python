import sys

dice = sys.stdin.readline
list = list(map(int, dice().split()))

if list[0] == list[1] == list[2]:
    print(list[0] * 1000 + 10000)

elif list[0] == list[1] and list[0] != list[2]:
    print(list[0] * 100 + 1000)

elif list[0] == list[2] and list[1] != list[2]:
    print(list[0] * 100 + 1000)

elif list[1] == list[2] and list[0] != list[2]:
    print(list[1] * 100 + 1000)

else:
    print(max(list) * 100)
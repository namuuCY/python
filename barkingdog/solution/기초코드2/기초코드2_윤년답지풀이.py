import sys

yr = int(input())

if yr % 4 == 0:
    if yr % 400 == 0:
        print(1)
    elif yr % 100 == 0:
        print(0)
    else:
        print(1)
else:
    print(0)

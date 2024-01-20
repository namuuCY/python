import sys

data = sys.stdin.readline().rstrip()
num = int(data)
string = str(data)

if num % 3 == 0:
    arr = list(string)
    arr.sort(reverse = True)
    
    if arr[-1] == '0':
        print(*arr, sep='')
    else:
        print(-1)

else:
    print(-1)
import sys

while True:
    data = str(sys.stdin.readline().rstrip())
    if data == '0 0 0':
        break
    L, P, V = list(map(int, data.split()))
    




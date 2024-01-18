import sys

ns = '0123456789'
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())

num = str(a * b * c)

for i in ns:
    print(num.count(i), end = '\n')
    

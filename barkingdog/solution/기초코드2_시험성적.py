import sys

pt = int(input())

if pt >= 90:
    print('A')
elif 80 <= pt <= 89:
    print('B')
elif 70 <= pt <= 79:
    print('C')
elif 60 <= pt <= 69:
    print('D')
else:
    print('F')
import sys

alpha = 'abcdefghijklmnopqrstuvwxyz'
cnt1 = [0] * 26
cnt2 = [0] * 26
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    str1, str2 = list(map(str, sys.stdin.readline().split()))           # map이라는 함수 반드시생각해야할듯?
    
    for i in range(26):
        cnt1[i] = str1.count(alpha[i])
    for i in range(26):
        cnt2[i] = str2.count(alpha[i])

    if cnt1 == cnt2:
        print('Possible')
        cnt1 = [0] * 26
        cnt2 = [0] * 26
    else:
        print('Impossible')
        cnt1 = [0] * 26
        cnt2 = [0] * 26


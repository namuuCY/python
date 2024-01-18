import sys

alph = 'abcdefghijklmnopqrstuvwxyz'
cnt1 = [0] * 26
cnt2 = [0] * 26


str1 = str(sys.stdin.readline().rstrip())
str2 = str(sys.stdin.readline().rstrip())

for i in range(26):
    cnt1[i] = str1.count(alph[i])
    cnt2[i] = str2.count(alph[i])

mincnt = [min(cnt1[i], cnt2[i]) for i in range(26)]

print( sum(cnt1) + sum(cnt2) - 2 * sum(mincnt))

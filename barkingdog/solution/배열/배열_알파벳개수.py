import sys

alph = 'abcdefghijklmnopqrstuvwxyz'

read = sys.stdin.readline

word = str(sys.stdin.readline().rstrip())

for i in range(len(alph)):
    print(word.count(alph[i]), end = ' ')
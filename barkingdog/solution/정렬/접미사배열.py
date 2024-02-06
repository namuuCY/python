import sys

word = sys.stdin.readline().rstrip()
data = []
data.append(word)
for i in range(1, len(word)):
    data.append(word[i:])

data.sort()

print('\n'.join(data))
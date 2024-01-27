import itertools

n, m = map(int, input().split())
data = list(set(map(int, input().split())))
data.sort()
anscomb = list(itertools.product(data, repeat = m))
anscomb.sort()

for i in anscomb:
    print(' '.join(map(str, i)))

import itertools

n,m  = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
comb = itertools.product(numbers, repeat = m)

for i in comb:
    print(*i, sep = ' ')
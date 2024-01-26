import itertools

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

comb = itertools.permutations(numbers, m)

for i in comb:
    print(*i, sep = ' ')

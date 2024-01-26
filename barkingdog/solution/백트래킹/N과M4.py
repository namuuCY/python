import itertools

n, m = map(int, input().split())

numbers = list(range(1, n + 1))

seqs = itertools.combinations_with_replacement(numbers, m)

for i in seqs:
    print(*i, sep = ' ')
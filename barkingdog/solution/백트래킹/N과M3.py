import itertools

n, m = map(int, input().split())

seqs = itertools.product(range(1, n + 1), repeat = m)
    
    # 이거 product가 집합사이의 데카르트곱임
    # 따라서 변수는 iterable이 두개거나
    # repeat = 2와 같이 되어야함.

for i in seqs:
    print(*i, sep = ' ')
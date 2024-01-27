import sys, itertools


while True:
    nums = sys.stdin.readline().rstrip()
    if nums == '0':
        break
    numbers = list(map(int, nums.split()))
    n = numbers[0]
    data = numbers[1:]
    comb = list(itertools.combinations(data, 6))
    for i in comb:
        print(*i, sep = ' ')
    print()

    
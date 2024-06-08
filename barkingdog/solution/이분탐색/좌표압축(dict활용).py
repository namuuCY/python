import sys

input()

numlist = list(map(int, sys.stdin.readline().split()))
sortednums = list(set(numlist))
sortednums.sort()
cardlist = {num: i for i, num in enumerate(sortednums)}

answer = [cardlist[num] for num in numlist]
sys.stdout.write(' '.join(map(str, answer)))
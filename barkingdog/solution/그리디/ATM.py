import sys
N = int(input())
times = list(map(int, sys.stdin.readline().split()))
times.sort()
print(sum((N - i) * times[i] for i in range(N)))
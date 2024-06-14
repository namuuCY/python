import sys

N = int(input())

data = list(map(int, sys.stdin.readline().split()))
ans = [0 for _ in range(N + 1)]

for i in range(N):
    ans[data[i]] = ans[data[i] - 1] + 1

print(N - max(ans))

'''import sys
N = int(input())
rope = list(map(int, sys.stdin.read().split()))
rope.sort()
ans = 0
for i in range(N):
    ans = max(ans, (N-i) * rope[i])
print(ans)'''

import io, os

def main():
    input = io.BufferedReader(io.FileIO(0), buffer_size=1 << 18).readline
    N = int(input())
    cnt = [0] * 10001
    for _ in range(N):
        cnt[int(input())] += 1
    i = 0
    print(max(ai * (i := i + cnt[ai]) for ai in range(10000, 0, -1)), flush=True)
    os._exit(0)

main()
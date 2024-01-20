import math, sys

n = int(input().rstrip())

for _ in range(n):
    ans = 0
    line = sys.stdin.readline().split()
    a = int(line[0])
    b = list(map(int, line[1:]))
    for i in range(len(b)):
        for j in range(i + 1, len(b)):
            ans += math.gcd(b[i], b[j])
    print(ans)



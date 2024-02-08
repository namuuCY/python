import sys
N, K = map(int, input().split())
coins = list(map(int, sys.stdin.read().split()))
coins.reverse()
D = []
i = 0
while True:
    D.append(K // coins[i])
    K -= coins[i] * D[-1]
    if K == 0:
        break
    i += 1
    
print(sum(D))

    
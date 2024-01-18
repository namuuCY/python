import sys

read = sys.stdin.readline


cnt = [0] * 2000000
ans = 0
n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline().rstrip())


for i in data:
    if i < x :
        cnt[i] += 1
        if cnt[x - i] == 1 and 2 * i != x:               # .x-i가 음수일수 있다. 이걸 어떻게 처리할까
            ans += 1

print(ans)
    


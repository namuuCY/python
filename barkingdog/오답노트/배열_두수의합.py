import sys

read = sys.stdin.readline


cnt = [0] * 2000000                                     # 지금 백만 단위의 숫자 안에서 OX퀴즈 하는거라 100만보다 좀더 넉넉하게 잡을 필요 있음. 메모리 충분 8메가임
ans = 0
n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline().rstrip())


for i in data:
    if i < x :
        cnt[i] += 1
        if cnt[x - i] == 1 and 2 * i != x:               # .x-i가 음수일수 있다. 이걸 어떻게 처리할까
            ans += 1                                        # x가 i의 2의 배수일 경우도 충분히 생각해줘야함.

print(ans)
    


# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 
# 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.
# 문제 링크 https://www.acmicpc.net/problem/3273

import sys

read = sys.stdin.readline


cnt = [0] * 2000000                                     # 지금 백만 단위의 숫자 안에서 OX퀴즈 하는거라 100만보다 좀더 넉넉하게 잡을 필요 있음. 메모리 충분 8메가임
ans = 0                                                 # 512MB =  1.2억개의 int임을 명심
n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline().rstrip())


for i in data:
    if i < x :
        cnt[i] += 1
        if cnt[x - i] == 1 and 2 * i != x:               # .x-i가 음수일수 있다. 이걸 어떻게 처리할까
            ans += 1                                        # x가 i의 2의 배수일 경우도 충분히 생각해줘야함.

print(ans)
    


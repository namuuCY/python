import sys
from collections import deque

Seq = deque()
ans = ""                # 굳이 ans를 리스트로 할필요도 없고,
cnt = 1                 # 굳이 number의 list를 뽑을 필요도없다.

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    t = int(sys.stdin.readline().rstrip())
    while cnt <= t:
        Seq.append(cnt)
        cnt += 1
        ans = '\n'.join([ans, '+'])         # join함수의 활용법 
    if Seq[-1] != t:
        print("NO")
        sys.exit(0)
    Seq.pop()
    ans = '\n'.join([ans, '-'])

print(ans)

    
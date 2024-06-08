import sys

N, M = map(int, input().split())

pokedicts = {}

for i in range(1, N + 1):
    name = sys.stdin.readline().strip()     # list는 hash불가능, 무조건 str화 할것!
    pokedicts[name] = str(i)                # strip()은 str로, split()은 list로 return함
    pokedicts[str(i)] = name

ans = []

for _ in range(M):
    ans.append(pokedicts[sys.stdin.readline().strip()])

sys.stdout.write('\n'.join(ans))
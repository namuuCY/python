import sys

i = 0
while True:
    data = str(sys.stdin.readline().rstrip())
    if data == '0 0 0':
        break
    L, P, V = list(map(int, data.split()))
    i += 1
    ans = (V // P) * L + min(V % P, L)
    print(f"Case {i}: {ans}")






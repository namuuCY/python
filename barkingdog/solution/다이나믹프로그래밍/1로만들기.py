n = int(input())

D = [0, 0]
for i in range(2, n + 1):
    tmp = []
    if i % 3 == 0:
        tmp.append(D[i // 3] + 1)
    if i % 2 == 0:
        tmp.append(D[i // 2] + 1)
    tmp.append(D[i - 1] + 1)
    D.append(min(tmp))

print(D[n])

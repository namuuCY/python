N = int(input())
D = [0, 0]# 0 0 1 1 2 3 2
preD = [0, 0]# 0 0 1 1 
if N >= 2:
    for i in range(2, N + 1):
        D.append(D[i - 1] + 1)
        preD.append(i - 1)
        if i % 2 == 0:
            if D[i] >= D[i // 2] + 1:
                D[i] = D[i // 2] + 1
                preD[i] = i // 2
        if i % 3 == 0:
            if D[i] >= D[i // 3] + 1:
                D[i] = D[i // 3] + 1
                preD[i] = i // 3
print(D[N])
ans = []
ans.append(N)
tmp = preD[N]
for _ in range(D[N]):
    ans.append(tmp)
    tmp = preD[tmp]
print(*ans, sep = ' ')


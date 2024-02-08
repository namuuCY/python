T = int(input())
D = []
D.append([1, 0])
D.append([0, 1])
for i in range(2, 41):
    D.append([D[i-1][0] + D[i-2][0], D[i-1][1]+ D[i-2][1]])

for _ in range(T):
    n = int(input())
    print(*D[n], sep = ' ')

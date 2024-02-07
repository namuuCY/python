D = {}
D[1] = 1
D[2] = 2
D[3] = 4 
trial = int(input().rstrip())
for n in range(4, 12):
    D[n] = D[n - 1] + D[n - 2] + D[n - 3]
for i in range(trial):
    print(D[int(input().rstrip())])
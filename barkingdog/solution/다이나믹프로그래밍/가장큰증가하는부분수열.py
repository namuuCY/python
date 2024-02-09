import sys

N = int(input())
seq = list(map(int, sys.stdin.readline().split()))

D = {seq[0]:seq[0]} # ~ 로 끝나는 증가하는 부분수열의 합
for i in range(1, N):
    tmp = []
    for e in D:
        if e < seq[i]:
            tmp.append(D[e] + seq[i])
    if not tmp:
        D[seq[i]] = seq[i]
    else:
        D[seq[i]] = max(tmp)
print(max(D.values()))
        


    




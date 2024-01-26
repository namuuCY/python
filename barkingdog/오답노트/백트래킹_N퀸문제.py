n = int(input())
                    #    시간을 로컬에서 측정할때는 반드시 release모드로 풀고 진행할것
isusedR = [True] * n           # true면 사용가능으로 바꾸는게 편한듯?
isusedD = [True] * (2 * n - 1)
isusedU = [True] * (2 * n - 1)

count = 0

def nqueen(k: int):
    global count
    if k == n:
        count += 1
        return
    for i in range(n):          # 논리구조를 헷갈림 주의할것.
        if isusedR[i] and isusedD[k+i] and isusedU[n-1-k+i]: 
            isusedR[i] = False
            isusedD[k+i] = False
            isusedU[n-1-k+i] = False
            nqueen(k + 1)
            isusedR[i] = True
            isusedD[k+i] = True
            isusedU[n-1-k+i] = True

nqueen(0)

print(count)

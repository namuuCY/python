n = int(input())


isusedR = [False] * n
isusedD = [False] * (2 * n -1)
isusedU = [False] * (2 * n -1)

count = 0

def placed(x: int, y: int) -> bool:
    return isusedR[y] and isusedD[x + y] and isusedU[n - 1 - x + y]

def nqueen(k: int):
    global count
    if k == n:
        count += 1
        return
    for i in range(n):
        if not placed(k, i):
            isusedR[i] = True
            isusedD[k+i] = True
            isusedU[n-1-k+i] = True
            nqueen(k + 1)
            isusedR[i] = False
            isusedD[k+i] = False
            isusedU[n-1-k+i] = False


nqueen(0)

print(count)

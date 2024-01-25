import sys

def threediv(x1: int, y1: int, n: int):
    global mcount, zcount, pcount
    
    mnum = sum(paper[i][j]== -1 for i in range(x1, x1 + n) for j in range(y1, y1+ n))
    znum = sum(paper[i][j]== 0 for i in range(x1, x1 + n) for j in range(y1, y1+ n))
    pnum = sum(paper[i][j]== 1 for i in range(x1, x1 + n) for j in range(y1, y1+ n))
    
    if mnum//(n ** 2) == 1 or znum // (n ** 2) == 1 or pnum//(n ** 2) == 1:
        mcount += mnum//(n ** 2)
        zcount += znum//(n ** 2)
        pcount += pnum//(n ** 2)
        return
    
    else:
        n1 = n//3
        threediv(x1, y1, n1)
        threediv(x1 + n1, y1, n1)
        threediv(x1 + 2 * n1, y1, n1)
        threediv(x1, y1 + n1, n1)
        threediv(x1 + n1, y1 + n1, n1)
        threediv(x1 + 2 * n1, y1 + n1, n1)
        threediv(x1, y1 + 2 * n1, n1)
        threediv(x1 + n1, y1 + 2 * n1, n1)
        threediv(x1 + 2 * n1, y1 + 2 * n1, n1)

mcount = 0
zcount = 0
pcount = 0
n =  int(input().rstrip())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

threediv(0,0,n)

print(mcount)
print(zcount)
print(pcount)










    

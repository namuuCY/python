import sys

mcount = 0
zcount = 0
pcount = 0
n =  int(input().rstrip())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def check(x: int, y: int, n:int):               # 같은지 확인하는거 걍 이건데...
    is_same = True
    for i in range(x, x + n):
        if not is_same:
            break
        for j in range(y, y + n):
            if paper[x][y] != paper[i][j]:
                is_same = False
                break
    if is_same:
        return True
    else:
        return False

def threediv(x1: int, y1: int, n: int):
    global mcount, zcount, pcount
    
    if check(x1, y1, n):
        if paper[x1][y1] == -1:
            mcount += 1
        elif paper[x1][y1] == 0:
            zcount += 1
        else:
            pcount += 1
    else:
        n1 = n // 3
        if n1 > 0:                              # 이거 표현법....
            for i in range(x1, x1+n, n1):       # + n1 = 1까지만이라고 써두면 좋다.
                for j in range(y1, y1+n, n1):
                    threediv(i, j, n1)


'''
        threediv(x1, y1, n1)
        threediv(x1 + n1, y1, n1)
        threediv(x1 + 2 * n1, y1, n1)
        threediv(x1, y1 + n1, n1)
        threediv(x1 + n1, y1 + n1, n1)
        threediv(x1 + 2 * n1, y1 + n1, n1)
        threediv(x1, y1 + 2 * n1, n1)
        threediv(x1 + n1, y1 + 2 * n1, n1)
        threediv(x1 + 2 * n1, y1 + 2 * n1, n1)
'''        


threediv(0,0,n)

print(mcount)
print(zcount)
print(pcount)










    

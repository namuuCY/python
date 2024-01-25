import sys

n = int(input().rstrip())
data = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
ansstr = []     # join으로 합칠계획이다.

def is_same(a: int, b: int, m: int):
    for i in range(a, a + m):
        for j in range(b, b + m):
            if data[a][b] != data[i][j]:
                return False
    else:
        return True
    
def quadtr(x: int, y: int, n: int):
    
    if is_same(x, y, n):
        ansstr.append(f'{data[x][y]}')      # 이거되는거임?
    else:
        ansstr.append('(')
        n2 = n // 2
        if n2 > 0:
            for i in range(x, x + n, n2):
                for j in range(y, y + n, n2):
                    quadtr(i, j ,n2)
        ansstr.append(')')
    

quadtr(0, 0, n)

ans = ''.join(ansstr)
print(ans)


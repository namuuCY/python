import sys

def chrtonum(i):
    if ord('0') <= ord(i) <= ord('9'): return int(i)
    else: return ord(i) - ord('A') + 10

def numtochr(j):
    if j < 10: return 'j'
    else: return chr(ord('A') + j - 10)

def numtoA(num):
    tmp = []
    if num < 36:
        return numtochr(num)
    while num != 1:
        tmp.append(numtochr(num % 36))
        num //= 36
        ans = reversed(tmp)
    return ans

def Atonum(a):
    length = len(a)
    num = 0
    for i in range(length):
        num += chrtonum(a[i]) * (36**(length - i - 1))
    return num

def Xall(val):
    ans = 0
    for i in range(len(strings)):
        for j in range(len(strings[i])):
            if strings[i][j] != val: continue
            ans += (chrtonum('Z') - chrtonum(strings[i][j])) * 36**(len(strings[i])-j)
    return ans


N = int(input())
strings = []
for _ in range(N):
    strings.append(list(sys.stdin.readline().rstrip()))
    
difflist = []
for i in range(36):
    difflist.append((Xall(numtochr(i)), numtochr(i)))

difflist.sort(key = lambda x: -x[0])

ans = 0
for j in range(len(strings)):
    ans += Atonum(strings[j])
for k in range(min(int(input()), 36)):
    ans += difflist[k][0]

print(''.join(numtoA(ans)))
    



    
            


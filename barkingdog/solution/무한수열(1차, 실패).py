def infseq(n: int, p: int, q: int) -> int:
    if n in D:
        return D[n]
    else:
        D[n] = infseq(n // p, p, q) + infseq(n // q, p, q)
        return D[n]
    
D = {}
D[0] = 1
n, p, q = map(int, input().split())

print(infseq(n,p,q))
    
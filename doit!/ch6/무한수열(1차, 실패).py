def infseq(n: int, p: int, q: int) -> int:
    if n == 0:
        return 1
    if n >= 1:
        return infseq(n // p, p, q) + infseq(n // q, p, q)
    

x = list(map(int, input().split()))
n, p, q = x

print(infseq(n,p,q))
    
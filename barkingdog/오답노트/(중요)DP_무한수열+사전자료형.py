# dict 자료형과 다이나믹 프로그래밍을 통해서 빠른 시간내로 가능.
# 재귀 깊이가 깊은경우에 이런거 써주니까 진짜 좋다.

def infseq(n: int, p: int, q: int) -> int:
    if n in D:          # 사전 자료형은 D[n]이라고 쓰면 있는거로 생각하고 keyerror일어남
        return D[n]     # n in D로 확인할것!
    else:
        D[n] = infseq(n // p, p, q) + infseq(n // q, p, q)
        return D[n]

D = {}
D[0] = 1
n, p, q = map(int, input().split())

print(infseq(n,p,q))
    
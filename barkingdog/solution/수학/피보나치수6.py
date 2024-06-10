

def prod(A, B):
    a1, a2, a3, a4 = A
    b1, b2, b3, b4 = B
    arr = [(a1*b1+a2*b3)%(1000000007), 
           (a1*b2+a2*b4)%(1000000007), 
           (a3*b1+a4*b3)%(1000000007), 
           (a3*b2+a4*b4)%(1000000007)]
    return arr

def pow(A, n):
    if n == 1:
        return A
    half = pow(A, n//2)
    if n % 2 == 0:
        return prod(half, half)
    else:
        return prod(prod(half, half), A)

N = int(input())

if N == 0: print(0)
elif N == 1: print(1)
else:
    A = [1,1,1,0]

    print(pow(A, N - 1)[0])
    

    
        

    


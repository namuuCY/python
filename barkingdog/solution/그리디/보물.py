# 재배열부등식 : 증가수열 두개의 곱의 합은 재배열된 것보다 크고
# 어느 한쪽을  reverse시킨 것의 곱, 즉 증가수열과 감소수열의 곱의 합보다는 재배열된게 크다


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse =  True)

print( sum(A[i] * B[i] for i in range(N)))
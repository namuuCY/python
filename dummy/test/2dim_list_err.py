n=3
m=4
arr=[[0]*m]*n
print(arr)      #여기까진 문제없어보임

arr[1][1]=5
print(arr)      # 이거 하면 결과값 [0500][0500][0500] 으로 나온다!
                # 왜냐면 [0]*m 의 동일한게 3개로 이뤄져있다고 생각하기 때문

#그래서 반드시
arr2=[[0]*m for _ in range(n)]
print(arr2)                     # 이거로 할것!
arr2[1][1]=5
print(arr2)
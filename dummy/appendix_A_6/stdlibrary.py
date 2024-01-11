# 표준 라이브러리
# itertools, heapq, bisect, collections, math

result=sum({3,4,4,5,6,7})
print(result)

result1=sum([3,4,4,5,6,7])
print(result1)

result2=sum((3,4,4,5,6,7))
print(result2)

ans1=min([1,4,4,5,2,1])
print(ans1)
ans2=max([1,4,4,5,2,1])
print(ans2)

ans3=eval("(3+5)*7")
print(ans3)

ans4=sorted((9,1,8,5,4), reverse=True)  #튜플을 넣으면 list가 나온다!
print(ans4)

ans4[2]+=1
print(ans4)

ans5=sorted([('홍',35),('박',75),('이',50)], key=lambda x: x[1], reverse=True)
print(ans5)

# 이렇게 정의하면 안됨ans6=sort([9,1,7,5,4])

dat1=[9,1,7,5,4]
#print(dat1.sort()) 이렇게 표현하려해도 안됨 
dat1.sort(reverse=True)
print(dat1)

from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

data=['A','B','C',"D"]
ans6=list( permutations(data,2) )
print(ans6)
ans7=list( combinations(data,2))
print(ans7)
ans8=list( product(data, repeat=2))
print(ans8)
ans9=list( combinations_with_replacement(data, 3))
print(ans9)
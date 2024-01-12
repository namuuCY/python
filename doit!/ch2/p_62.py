
print(type((1,2,3)))

print(id([1,2,3]))
print(id([1,2,3,4]))
print(id([1,2,3,5]))

#   b=3,                #이렇게 쓰면 b는 튜플로 설정된거라 append 불가능







print(list(range(5)))
print(tuple(range(6)))


data2=tuple(map(int,input().split()[:3]))  
print(data2)
data=list(map(int,input().split()[:5]))      #외워둘것. 많은 양의 정보가 input될때 상당이 유용

total=sum(data)
print(f"합계는 {total}")
print(f"평균은 {total/5}")

data.sort()
print(data)


data.sort(reverse=True)
print(data) 
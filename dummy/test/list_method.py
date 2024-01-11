a= [1,7,3,5,2,4,3,3,2,1]

a.append(2)
print("삽입: ", a)

a.sort()
print("오름차순 : ", a)

a.sort(reverse=True)        #앞에 대문자를 True 라고 반드시 써야하네
print("내림차순 : ", a)

a= [1,7,3,5,2,4,3,3,2]

a.reverse()
print("원소 뒤집기 : ", a)

a.insert(2,1)                       #마찬가지로 숫자에 주의, 인덱스가 2니까 세번째 자리에 들어간다
print("인덱스 2에 1추가 : ", a)        # insert는 시간복잡도가 은근 높아서 시간잡아먹는다

print("값이 3인 데이터 개수 : ", a.count(3))

a.remove(1)
print("값이 1인 데이터 삭제 : ", a)     #특이사항 : 리스트 전체의 개수가 줄어든다.

remove_set={3,2}
result = [i for i in a if i not in remove_set]       #특이사항 : i | i는 a에 있으면서 remove_set에 없는것, 마치 수학적표현
print(result)
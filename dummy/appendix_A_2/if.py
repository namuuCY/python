x=15
if x>=10:
    print(x)

pt=85
if pt>=90:
    print("학점 : A")
elif pt>=80:
    print("학점 : B")
elif pt>=70:
    print("학점 : C")
else:
    print("학점 : F")


if pt >=70:
    print("성적이 70점이상")
    if pt >=85:                     #들여쓰기 표준은 스페이스바 4번인데 탭쓰셈 시험때는
        print("우수한 성적임")       #아니근데 이게뭐라고
else:
    print("님 성적 별로임")
    print("분발하셈")


print("프로그램 종료")

if pt>= 80:
    pass
else:
    print("성적이 80점 미만")

#신기한거ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

if pt >= 80: result="success"
else : result="Fail"
print(result)


# 더 줄인버전
arr="Success" if pt >= 75 else "Fail"
print(arr)


a=[1,1,2,3,4,5,5,3]
rem_set={3,5}               #제거할 set은 집합인것을 주의하자

result1=[]
for i in a:
    if i not in rem_set:
        result1.append(i)
print(result1)

k=75
superk=k if 60<k<80 else 0
print(superk)
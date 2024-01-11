ans=14
print("정답은", ans, "입니다.")  # 이경우 , 대신 공백들어간다 결과값에 띄어쓰기나옴
print(f"정답은 {ans}입니다.")


n=int(input())
data=list( map(int, input().split()))  #이거 꼭 외우고 있기  input().split() 이다 쉼표아님!



# 위 코드는 n개의 정수입력받고, 각각의 정수를 (int화)' '(int화)''... 이꼴로 만들어주는것\
# 그리고 저기서 split은 프로그램 돌렸을때 space바를 써야한다는것임
# 즉, 공백이 기준으로 입력되는것


data.sort(reverse=True)
print(data)

n,m,k=map(int, input().split())
print(n,m,k)

import sys
data1=sys.stdin.readline().rstrip() # 입력하는게 많을때 이거써!
print(data1)




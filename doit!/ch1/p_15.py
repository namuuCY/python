print("세 정수의 최댓값?")
a=int(input('정수 a값? : '))
b=int(input('정수 b값? : '))
c=int(input('정수 c값? : '))

maximum=a
if b>maximum: maximum=b
if c>maximum: maximum=c

print(f"최댓값은 {maximum}입니다.")
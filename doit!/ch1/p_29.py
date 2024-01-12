print("a부터 b까지의 합?")
a= int(input("a값입력"))
b= int(input("b값입력"))
c= int(input("c값입력"))

if a>b:
    a,b=b,a                     #오름차순 정렬

sum=0


for i in range(a,b+1):
    if i<b:
        print(f"{i}+",end='')              #range(n)은 그자체로 시퀀스가 아님
    else:                                       #range (n)은 0부터 n-1까지만 보여줌
        print(f"{i}=", end='')
    sum+=i                      

print(sum)


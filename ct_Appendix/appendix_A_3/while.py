i=1
result=0

while i<9:
    result+=i
    i+=1

print(result)

result1=0
i=0

while i<9:
    if i%2==1:
        result1+=i
    i+=1
    
print(result1)

result=0
for i in range(1,20):   #마지막 숫자 20은 뺀다!
    result +=i

print(result)

score=[90,85,77,65,97]
for i in range(5):
    if score[i]>=80:
        print(i+1, "번 학생은 합격입니다!")

cheat_list={2,4}
for i in range(5):               #별일없으면 range(5) 숫자 하나로 시작하는건 0부터 시작, 4까지
    if i+1 in cheat_list:
        continue
    if score[i]>=80:
        print(i+1,"번 학생은 합격입니다!") 

# \n 대신 print() 집어넣네    
        
for i in range(2,10):
    for j in range(1,10):
        print(i,"X",j,"=",i*j)
    print()
    


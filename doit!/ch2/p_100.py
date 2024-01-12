#두번째 방법
counter=0
pn=[2,3,7,11,13,17]

for n in range(19,1001,2):
    for i in pn :
        if i * i > n:
            break
        counter+=1
        if n % i ==0:
            break
    else:
        pn.append(n)

print(pn)
print(counter)
        
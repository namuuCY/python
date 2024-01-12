#두번째 방법
counter=0
pn=[2,3]

for n in range(5,1001,2):
    for i in range(len(pn)) :
        counter+=1
        if n % pn[i] == 0:
            break
    else:
        pn.append(n)

print(pn)
print(counter)
        
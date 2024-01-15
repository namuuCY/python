#두번째 방법

pn=[2,3]

for n in range(5,1001,2):
    i = 0
    while pn[i] * pn[i] <= n:           # 어떤 조건을 걸고
        if n % pn[i] == 0:
            break
        i += 1
    else:
        pn.append(n)                    # 저 조건을 충족하지 않으면 등록
    

print(pn)

        
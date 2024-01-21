n = int(input())

limit = n // 5
found = False

for i in range(limit, -1, -1):          
    if (n - 5 * i) % 3 == 0:
        print(i + (n - 5 * i) // 3)
        found = True
        break

if not found:
    print(-1)

# 아래에서 4, 7에서 방법찾지못했을때 해결책 제시해줌
# yes no 찾을때 bool 함수 이용하는게 생각보다 괜찮은듯?

#n = int(input())

#if n==4 or n == 7:
#    print(-1)
    
#limit = n // 5 

#for i in range(limit, -1, -1):
#    if n - 5 * i >= 0:
#        if (n - 5 * i) % 3 == 0:
#            ans = i + (n - 5 * i) // 3
#            print(ans)
#            break
        
            
#    else:
#        print(-1)
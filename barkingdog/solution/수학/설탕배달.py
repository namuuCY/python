n = int(input())

if n==4 or n == 7:
    print(-1)
    
limit = n // 5 

for i in range(limit, -1, -1):
    if n - 5 * i >= 0:
        if (n - 5 * i) % 3 == 0:
            ans = i + (n - 5 * i) // 3
            print(ans)
            break
        
            
    else:
        print(-1)
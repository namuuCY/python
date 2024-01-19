from collections import deque
import sys

stack = deque()
n = int(input())
count = 0
for _ in range(n):
    k = int(sys.stdin.readline().rstrip())
    if stack:
        while stack and stack[-1] <= k:
            if stack[-1] == k:
                count += 1
                break
            else: 
                stack.pop()
                count += 1
            
            
        if stack:
            stack.append(k)
            count += 1
            
        else:
            stack.append(k)
            

    else:
        stack.append(k)
        

print(count)
        
            






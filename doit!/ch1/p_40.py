m=int(input("원하는 *의 개수?"))
j=int(input("몇개마다 줄바꿈?"))

for _ in range(m//j):
    print('*'*j)
    print()

print('*'*(m%j))





print("+와 - 를 번갈아가면서 출력")
n=int(input("원하는 개수?"))

for  _ in range(n//2):
    print("+-",end='')


if n%2 :
   print("+")






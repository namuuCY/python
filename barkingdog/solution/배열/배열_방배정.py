import sys
import math

data = sys.stdin.readline().rstrip()
people, room = map(int, data.split())

div = [[0] * 2 for _ in range(6)]

for i in range(people):
    line = sys.stdin.readline().rstrip()
    a,b = map(int, line.split())
    b -= 1
    div[b][a] += 1

for i in range(6):
    for j in range(2):
        div[i][j] = math.ceil(div[i][j] / room) 

sum = 0

for i in range(6):
    for j in range(2):
        sum += div[i][j] 
print(sum)
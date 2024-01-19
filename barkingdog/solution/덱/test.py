from collections import deque
import sys, json


a = [1,2,3,4]

print(type(a))
print(a)

b = deque(a)
print(b)

seq = sys.stdin.readline().rstrip()
print(type(seq))
list = json.loads(seq)
print(type(list))
print(list)

print
print(*list, sep='')

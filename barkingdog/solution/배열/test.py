from typing import MutableSequence

def insert(value: int, key: int, a: MutableSequence) -> None:
    length = len(a)
    a.append(0)
    for i in range(length, key, -1):
        a[i] = a[i - 1]
    a[key] = value

def erase(idx: int, a: MutableSequence) -> MutableSequence:
    return a[:idx] + a[idx+1 : ]
    

    

c = [[0]*4 for _ in range(5)]

c[1][2] = 1

print(c)
a= [1,2,3,4,5,7,8,9]

insert(6, 5, a)
b= erase(2, a)
print(*b, sep = ' ')


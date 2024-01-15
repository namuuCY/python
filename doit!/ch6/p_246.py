from typing import MutableSequence
import bisect

def binary_insertion_sort(a: MutableSequence) -> None:

    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)


if __name__=='__main__':
    print('이진 삽입 정렬 수행')
    num = int(input('원소의 수? '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    binary_insertion_sort(x)

    print("오름차순 정렬 완료")

    for i in range(num):
        print(f'x[{i}] = {x[i]}')
        
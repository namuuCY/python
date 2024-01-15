from typing import MutableSequence
import bisect

def binary_insertion_sort(a: MutableSequence) -> None:

    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)        # bisect.insort(a, x, lo, hi)
                                                # a 라는 정렬에 x를 a[lo]와 a[hi]  사이에 집어넣는다는 뜻
                                                # a.pop(i)는 주어진 리스트에서 i번째 인덱스를 가진 요소를 아예 값을 빼버리고 리스트를 줄임
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
        
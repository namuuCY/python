from typing import MutableSequence

def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int):

    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2] 
    if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3] 
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2] 
    return idx2

def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
    for i in range(left + 1, right + 1):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

def qsort(a: MutableSequence, left: int, right: int) -> None:
    if right - left < 9:
        insertion_sort(a, left, right)
    else:
        pl = left
        pr = right
        m = sort3(a, pl, (pl + pr) // 2, pr)
        x = a[m]

        a[m], a[pr - 1] = a[pr - 1], a[m] 
        pl += 1
        pr -= 2
        while pl <= pr:
            while a[pl]
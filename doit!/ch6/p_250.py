from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    
    n = len(a)
    h = n // 2

    while h > 0:
        for i in range(h, n):
            j = i - h
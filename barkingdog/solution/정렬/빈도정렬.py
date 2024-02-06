import sys
from collections import Counter

#중요. list.sort( ~~ lambda ~~ list.(list관련함수)) 는 동작하지 않음!
# 왜냐하면 list를 sort하는 동안 일시적으로 list가 잠겨있기 때문에그렇슴
# 따라서 아래 답변처럼 sorted로 새로 설정하고 하면 문제해결됨.

N, C = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
freq = Counter(arr)

new_arr = sorted(arr, key=lambda x: (-arr.count(x), arr.index(x)))

print(new_arr)
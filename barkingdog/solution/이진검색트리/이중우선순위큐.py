import sys
import bisect

input = sys.stdin.read
data = input().split()

index = 0
num_cases = int(data[index])
index += 1
results = []

for _ in range(num_cases):
    dual_Q = []
    num_queries = int(data[index])
    index += 1

    for _ in range(num_queries):
        query, num = data[index], data[index + 1]
        index += 2
        num = int(num)

        if query == 'I':
            bisect.insort_right(dual_Q, num)
        elif dual_Q:
            if num == -1:
                dual_Q.pop(0)
            else:
                dual_Q.pop(-1)

    if not dual_Q:
        print('EMPTY')
    else:
        print(f"{dual_Q[-1]} {dual_Q[0]}")

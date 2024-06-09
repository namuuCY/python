import bisect, sys


def insert(dual_Q, val):
    bisect.insort_right(dual_Q, val)

'''def search(dual_Q, val):
    index = bisect.bisect_left(dual_Q, val)
    if index != len(dual_Q) and dual_Q[index] == val:
        return 


def delete(dual_Q, val):
    index = bisect.bisect_left(dual_Q, val)
    if index != len(dual_Q) and dual_Q[index] == val:
        dual_Q.pop(index)
        return 
    return '''


for _ in range(int(input().rstrip())):
    dual_Q = []         # 새로 초기화할 필요는 없다. 
    for _ in range(int(input().rstrip())):
        querry, num = sys.stdin.readline().split()
        if querry == 'I':
            insert(dual_Q, int(num))
        elif not dual_Q:
            continue
        else:
            if num == '-1':
                dual_Q.pop(0)
            else:
                dual_Q.pop(-1)

    if not dual_Q:
        print('EMPTY')
    else:
        print(dual_Q[-1], dual_Q[0])

        


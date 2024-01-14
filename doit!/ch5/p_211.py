pos = [0] * 8
flag1 = [False] * 8
flag2 = [False] * 15
flag3 = [False] * 15

def put() -> None:

    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()


def set(i: int) -> None:

    for j in range(8):
        if(    not flag1[j]
            and not flag2[i + j]
            and not flag3[i - j + 7]):
            pos[i] = j
            if i == 7 :
                put()
            else:
                flag1[j] = flag2[i + j] = flag3[i - j + 7] = True
                set(i + 1)
                flag1[j] = flag2[i + j] = flag3[i - j + 7] = False
            

set(0)
def stars(n: int):
    if n == 3:
        return ['  *  ', ' * * ','*****']
    else:
        St = stars(n // 2)
        star = []
        for i in St:
            star.append(' ' * (n//2) + i + ' ' * (n//2))
        for i in St:
            star.append(i + ' ' + i)
    return star

n = int(input())
print('\n'.join(stars(n)))


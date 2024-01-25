asdf = set([1,2,3,4,5])
while True:
    asdf_iter = iter(asdf)
    a = next(asdf_iter, False)
    if not a:
        print('exit')
        break
    print(a)
    
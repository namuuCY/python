x=('jo','ge','pa','ri')

for i in x:
    print(i)

for i, name1 in enumerate(x,1):
    print(f'{i}번째 = {name1}')

for i, name in enumerate(x):
    print(f'x[{i}]={name}')



for i in range(len(x)):
    print(f'x[{i}]= {x[i]}')
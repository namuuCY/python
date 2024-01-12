from ssearch import seq_search


t=(4,7,5.6,2,3.14,1)
s='string'
a=['DTS','AAC','FLAC']



number=0
x=[]

while True:
    s=input(f'x[{number}]')
    if s=='end':
        break
    x.append(float(s))
    number+=1

ky=float(input('검색할 값을 입력하세요: '))

idx=seq_search(x,ky)
if idx==-1:
    print('검색값 없음')
else:
    print(f'x[{idx}]에 있음')

import sys

nums = '0123456789'

cnt = [0] * 10

string = str(sys.stdin.readline().rstrip())

for i in string:
    cnt[int(i)] = string.count(i)

sixnine = (cnt[6] + cnt[9] + 1) // 2
new_cnt = cnt[:6] + cnt[7:9]

if  sixnine > max(new_cnt):           # 6,9를 제외하고 count값의 최대를 계산해줘야함.
    print(sixnine)               # 예를 들어 666699면 max는 4인데 저거 3세트만필요함
else:
    print(max(new_cnt))

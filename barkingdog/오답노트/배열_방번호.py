# 다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.
# 다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 
# 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)
# 문제 링크 https://www.acmicpc.net/problem/1475

import sys

nums = '0123456789'

cnt = [0] * 10

string = str(sys.stdin.readline().rstrip())

for i in string:
    cnt[int(i)] = string.count(i)

sixnine = (cnt[6] + cnt[9] + 1) // 2
new_cnt = cnt[:6] + cnt[7:9]            # <<<<<< 이부분은 리스트를 새로 append하는 방법도 있음.

if  sixnine > max(new_cnt):           # 6,9를 제외하고 count값의 최대를 계산해줘야함.
    print(sixnine)               # 예를 들어 666699면 max는 4인데 저거 3세트만필요함
else:
    print(max(new_cnt))

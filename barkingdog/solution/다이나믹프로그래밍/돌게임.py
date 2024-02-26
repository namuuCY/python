N = int(input())

DP = {1:1, 2:0, 3:1}

if N >= 4:
    for i in range(4, N + 1):
        DP[i] = min((DP[i - 1] + 1) % 2, (DP[i - 3] + 1) % 2)

if DP[N] == 1:
    print('SK')
else:
    print('CY')




'''야매풀이
if N % 2 == 1:
    print('SK')
else:
    print('CY')
'''
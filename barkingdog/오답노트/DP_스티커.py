import sys

T = int(input())

for _ in range(T):
    n = int(input())
    card = []
    for _ in range(2):
        card.append([0] + list(map(int, sys.stdin.readline().split())))
    DP = [[0 for _ in range(n + 1)] for _ in range(2)]
    DP[0][1] = card[0][1]
    DP[1][1] = card[1][1]
    if n >= 2:                      # 2차원배열이라고 항상 for문 2개 있는거 아님!
        for i in range(2, n + 1):   # index 끝값처리
            DP[0][i] = max(DP[0][i - 2], DP[1][i - 2], DP[1][i - 1]) + card[0][i]
            DP[1][i] = max(DP[1][i - 2], DP[0][i - 2], DP[0][i - 1]) + card[1][i]
    print(max(DP[0][n], DP[1][n]))                        # 복붙할때 값바꾸는거 잊지말기


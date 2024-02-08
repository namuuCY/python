N, K = map(int, input().split())
stuff = [list(map(int, input().split())) for _ in range(N)] #무게, 가치
rotate = [list(row) for row in zip(*stuff)]
Weight = [0] + rotate[0]
Value = [0] + rotate[1]

DP = [[0 for _ in range(K + 1)] for _ in range(N + 1)] # [i][j] 물건개수 i개, 무게 j일때 최대값

def dynamic(K, Weight, Value):
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if Weight[i] > j:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = max(DP[i - 1][j] , DP[i - 1][j - Weight[i]] + Value[i])
    return DP[N][K]

ans = dynamic(K, Weight, Value)

print(ans)
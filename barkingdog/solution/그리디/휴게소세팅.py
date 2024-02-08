# 그리디 아닙니다.

N, M, L = map(int, input().split())
station = [0] + list(map(int, input().split())) + [L]
station.sort()

print(*list(station[i]-station[i - 1] for i in range(1, N + 2)))
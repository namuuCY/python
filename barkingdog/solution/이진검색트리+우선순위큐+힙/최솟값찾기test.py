from collections import deque

N, L = map(int, input().split())  # 수열의 길이 N과 윈도우의 길이 L을 입력받습니다.
seq = list(map(int, input().split()))  # 전체 수열을 입력받습니다.
ans = []
deq = deque()

for i in range(N):
    # 덱의 첫 번째 인덱스가 윈도우 범위를 벗어나면 제거합니다.
    if deq and deq[0] < i - L + 1:
        deq.popleft()

    # 새로운 요소가 덱의 마지막 요소의 값보다 작으면, 그보다 큰 값들을 덱에서 제거합니다.
    while deq and seq[deq[-1]] > seq[i]:
        deq.pop()

    deq.append(i)

    # 윈도우가 완전히 채워진 후부터 결과 리스트에 최소값을 추가합니다.

    ans.append(seq[deq[0]])

print(*ans)
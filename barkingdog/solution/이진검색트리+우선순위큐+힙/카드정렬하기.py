import sys, heapq


N = int(input())
cards = list(map(int, sys.stdin.read().split()))

ans = 0

if N == 1:
    print(ans)

else:
    heapq.heapify(cards)
    
    for _ in range(N - 1):
        card1 = heapq.heappop(cards)
        card2 = heapq.heappop(cards)
        ans += (card1 + card2)
        heapq.heappush(cards, card1 + card2)

    print(ans)

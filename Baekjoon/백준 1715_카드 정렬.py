import sys
import heapq
sys.stdin = open('1715.txt', 'r')

N = int(input())
cards = []
for _ in range(N):
    cards += [int(input())]

heapq.heapify(cards)

ans = 0
while len(cards) > 1:
    x, y = heapq.heappop(cards), heapq.heappop(cards)

    ans += x + y
    heapq.heappush(cards, x + y)

print(ans)

from heapq import *

n, m = map(int, input().split())
card_list = list(map(int, input().split()))
heapify(card_list)

for _ in range(m) :
  a = heappop(card_list)
  b = heappop(card_list)
  heappush(card_list, a+b)
  heappush(card_list, a+b)

print(sum(card_list))
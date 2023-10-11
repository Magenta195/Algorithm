from heapq import heapify, heappush, heappop
import sys
input = sys.stdin.readline

N, k = map(int, input().split())
casher_list = list()
empty_casher_list = list(range(k))
heapify(empty_casher_list)
answer = 0
idx, prev_t = 1, 0

for _ in range(N) :
  id, w = map(int, input().split())
  if len(casher_list) == k :
    prev_t = casher_list[0][0]
    while casher_list and casher_list[0][0] == prev_t :
      _, prev_casher, prev_id = heappop(casher_list)
      heappush(empty_casher_list, -prev_casher)
      answer += idx*prev_id
      idx += 1
  heappush(casher_list, (prev_t + w, -heappop(empty_casher_list), id))

while casher_list :
  _, _, prev_id = heappop(casher_list)
  answer += idx*prev_id
  idx += 1

print(answer)
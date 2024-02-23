from collections import defaultdict
from heapq import *
import sys

input = sys.stdin.readline


def solve():
  N, K = map(int, input().split())
  count = defaultdict(int)
  count[1] += K - 1
  count[N - K + 1] += 1
  q = list(count.keys())
  heapify(q)
  ans = 0
  
  while sum(count.values()) > 1:
    if count[q[0]] > 1:
      key, val = q[0] * 2, count[q[0]] // 2
      if key not in count:
        heappush(q, key)
      count[key] += val
      count[q[0]] %= 2
      if count[q[0]] == 0:
        heappop(q)
      ans += key * val
    else:
      key = heappop(q)
      sec_key = q[0]
      count[key] -= 1
      count[sec_key] -= 1
      if key + sec_key not in count:
        heappush(q, key + sec_key)
      count[key + sec_key] += 1
      ans += key + sec_key
      if count[sec_key] == 0:
        heappop(q)
  print(ans)

for _ in range(int(input())) :
  solve()
from collections import deque
import sys
input = sys.stdin.readline

def solve() :
  global L
  N, L, K = map(int, input().split())
  ants = list()
  for _ in range(N) :
    p, a = map(int, input().split())
    if a > 0 :
      p = L - p
    ants.append([p, a])
  result = list()
  idx_q = deque()
  fall_q = deque()

  for p, idx in ants :
    if idx > 0 :
      idx_q.append(idx)
      fall_q.append(p)
    else :
      idx_q.append(idx)
      fall_q.append(p)
      result.append((fall_q.pop(), idx_q.popleft()))
  while idx_q and fall_q :
    result.append((fall_q.pop(), idx_q.pop()))
  result.sort()
  print(result[K-1][-1])

for _ in range(int(input())) :
  solve()

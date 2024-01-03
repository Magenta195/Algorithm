from collections import deque
import sys
input = sys.stdin.readline

def solve() :
  global L
  N, L, K = map(int, input().split())
  idx_q = deque()
  fall_q = deque()
  result = list()
  for _ in range(N) :
    p, idx = map(int, input().split())
    if idx > 0 :
      p = L - p
    idx_q.append(idx)
    fall_q.append(p)
    if idx < 0  :
      result.append((fall_q.pop(), idx_q.popleft()))
  while idx_q and fall_q :
    result.append((fall_q.pop(), idx_q.pop()))
  result.sort()
  print(result[K-1][-1])

for _ in range(int(input())) :
  solve()
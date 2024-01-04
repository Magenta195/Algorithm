from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
runners = [int(input()) for _ in range(N)]
rank = sorted(runners)
runners = [bisect_left(rank, r)+1 for r in runners]
tree = [0] * (N+1)

def search(idx, length) :
  result = 0
  while idx :
    result += tree[idx]
    idx -= idx & -idx
  print(length + 1 - result)

def update(idx) :
  while idx <= N :
    tree[idx] += 1
    idx += idx & -idx

for i in range(N) :
  search(runners[i], i)
  update(runners[i])
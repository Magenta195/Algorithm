from collections import defaultdict
import sys
input = sys.stdin.readline
MAX = float('inf')

N, Q, K = map(int, input().split())
A = list(map(int, input().split()))
odd_type = defaultdict(lambda : (-MAX, -MAX))
odd_sum = [0, 0]
odds = [K//2 + K%2, K//2]
sums = sum(A[:K])
for i in range(N) :
  idx = tuple(odds)
  if odd_type[idx] < (sums, -i-1) :
    odd_type[idx] = (sums, -i-1)
  sums += A[(i+K)%N] - A[i]
  odds[(i+K)%N%2] += 1
  odds[i%2] -= 1

for _ in range(Q) :
  q, *cmd = map(int, input().split())
  if q == 1 :
    odd_sum[0] += cmd[0]
  elif q == 2 :
    odd_sum[1] += cmd[0]
  else :
    maxval = (-MAX, -MAX)
    for key, val in odd_type.items() :
      val = (val[0] + odd_sum[0]*key[0] + odd_sum[1]*key[1], val[1])
      if maxval < val :
        maxval = val
    print(-maxval[1], maxval[0])
from heapq import *
import sys
input = sys.stdin.readline
MAX = float('inf')

def solve() :
  N = int(input())
  start = int(input())-1
  dist_sums = [0]
  for _ in range(N-1) :
    dist_sums.append(dist_sums[-1] + int(input()))
  dp = [[[MAX]*2 for _ in range(N)] for _ in range(N)]
  dp[start][start][0] = dp[start][start][1] = 0
  q = [(0, 0, start, start)]
  while q :
    cost, point, left, right = heappop(q)
    if (left, right) == (0, N-1) :
      return cost
    for np, nleft, nright in [(0, left-1, right), (1, left, right+1)] :
      if 0 <= nleft and nright <= N-1 : 
        cur = right if point else left
        next = nright if np else nleft
        next_cost = cost + abs(dist_sums[cur] - dist_sums[next]) * (N - (right-left+1))
        if dp[nleft][nright][np] > next_cost :
          dp[nleft][nright][np] = next_cost
          heappush(q, (next_cost, np, nleft, nright))

for _ in range(int(input())) :
  print(solve())
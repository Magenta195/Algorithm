from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())

construct_dict = defaultdict(set)
for _ in range(K) :
  a, b, c, d = map(int, input().split())
  construct_dict[(a, b)].add((c, d))
  construct_dict[(c, d)].add((a, b))

dp = [[0]*(N+1) for _ in range(M+1)]
dp[0][0] = 1

for y in range(M+1) :
  for x in range(N+1) :
    if y > 0 and ((x, y) not in construct_dict or (x, y-1) not in construct_dict[(x, y)]) :
      dp[y][x] += dp[y-1][x]
    if x > 0 and ((x, y) not in construct_dict or (x-1, y) not in construct_dict[(x, y)]) :
      dp[y][x] += dp[y][x-1]
      
print(dp[-1][-1])
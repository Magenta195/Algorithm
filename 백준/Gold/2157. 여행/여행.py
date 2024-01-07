from collections import defaultdict
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

flight_course = defaultdict(list)
for _ in range(K) :
  a, b, c = map(int, input().split())
  if a > b :
    continue
  flight_course[a].append((b, c))

dp = [[-1]*M for _ in range(N+1)]

dp[1][-1] = 0
for i in range(1, N) :
  for j in range(1, M) :
    if dp[i][j] == -1 :
      continue
    for nxt, cost in flight_course[i] :
      dp[nxt][j-1] = max(dp[nxt][j-1], dp[i][j] + cost)

print(max(dp[-1]))
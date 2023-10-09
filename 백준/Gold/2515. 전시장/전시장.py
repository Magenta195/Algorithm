import sys
input = sys.stdin.readline
MAX = float('inf')

N, S = map(int, input().split())
picture_list = [[0, 0]] + sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x : (x[0], -x[1]))
dp = [-MAX]*(N+1)
dp[0] = 0
prev_max, prev_idx = 0, 0
for i in range(1, N+1) :
  for j in range(prev_idx, i) :
    if picture_list[i][0] - picture_list[j][0] < S :
      break
    prev_idx = j
    prev_max = max(prev_max, dp[j])
    dp[i] = max(dp[i], prev_max + picture_list[i][1])

print(max(dp))
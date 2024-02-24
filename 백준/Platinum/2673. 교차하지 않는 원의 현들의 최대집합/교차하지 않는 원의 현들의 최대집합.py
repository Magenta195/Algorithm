import sys
input = sys.stdin.readline
MAX = 101
N = int(input())
lines = [[0]*MAX for _ in range(MAX)]

for _ in range(N) :
  a, b = map(int, input().split())
  lines[a][b] = lines[b][a] = 1

dp = [[0]*MAX for _ in range(MAX)]

for i in range(1, MAX-1) :
  for j in range(1, MAX-i) :
    for k in range(j, j+i) :
      dp[j][j+i] = max(dp[j][j+i], dp[j][k] + dp[k][j+i] + lines[j][j+i])
print(dp[1][100])
import sys
input = sys.stdin.readline
MAX = float('inf')

N, B = map(int, input().split())
machines = []

for i in range(N) :
  p, a, b = map(int, input().split())
  c = 0
  tmp = []
  while True :
    if p > 100 :
      tmp.append((100, c))
      break
    tmp.append((p, c))
    p += a
    c += b
  machines.append(tmp)

dp = [[(0, 0, 0)]*(B+1) for _ in range(N+1)]
dp[0][0] = (1, 0, 0)

for i in range(N) :
  for j in range(B+1) :
    if dp[i][j] == (0, 0, 0) :
      continue
    for idx, (p, c) in enumerate(machines[i]) :
      if j+c > B :
        break
      if dp[i+1][j+c][0] < dp[i][j][0] * p :
        dp[i+1][j+c] = (dp[i][j][0] * p, idx, j)

idx = dp[-1].index(max(dp[-1]))
print(dp[-1][idx][0])
result = []
for i in range(N, 0, -1) :
  result.append(dp[i][idx][1])
  idx = dp[i][idx][2]
print(*reversed(result))

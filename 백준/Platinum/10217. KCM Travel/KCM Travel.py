import sys
input = sys.stdin.readline
MAX = float('inf')
_ = int(input())

N, M, K = map(int, input().split())
node_list = [[] for _ in range(N+1)]
dp = [[MAX]*(M+1) for _ in range(N+1)]
dp[1][0] = 0
for _ in range(K) :
  u, v, c, d = map(int, input().split())
  node_list[u].append((v, c, d))

for cost in range(M+1) :
  for node in range(N+1) :
    if dp[node][cost] < MAX :
      for nxt, ncost, ntime in node_list[node] :
        ntime += dp[node][cost]
        ncost += cost
        if ncost <= M and ntime < dp[nxt][ncost] :
          dp[nxt][ncost] = ntime

result = min(dp[N])
print("Poor KCM" if result == MAX else result)
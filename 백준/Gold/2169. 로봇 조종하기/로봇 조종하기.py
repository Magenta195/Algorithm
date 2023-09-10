import sys
input = sys.stdin.readline
MAX = float('inf')
N, M = map(int, input().split())
value_list = [list(map(int, input().split())) for _ in range(N)]
dp = [[-MAX]*M for _ in range(N)]
for i in range(M) :
  if i == 0 :
    dp[0][i] = value_list[0][i]
  else :
    dp[0][i] = dp[0][i-1] + value_list[0][i]

for i in range(1, N) :
  Ldp, Rdp = [-MAX]*M, [-MAX]*M
  Ldp[0] = dp[i-1][0] + value_list[i][0]
  Rdp[-1] = dp[i-1][-1] + value_list[i][-1]
  for j in range(1, M) :
    Ldp[j] = max(Ldp[j-1], dp[i-1][j]) + value_list[i][j]
    Rdp[-1-j] = max(Rdp[-j], dp[i-1][-1-j]) + value_list[i][-1-j]
  for j in range(M) :
    dp[i][j] = max(Ldp[j], Rdp[j])
        
print(dp[-1][-1])
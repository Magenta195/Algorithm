N, M = map(int, input().split())

def gcd(a, b) :
  ta, tb = a, b
  while b :
    a, b = b, a % b
  return ta // a, tb // a

dp = [[0]*(N+1) for _ in range(N+1)]
dp[1][1] = 1

for i in range(1, N) :
  for j in range(1, i+1) :
    dp[i+1][j+1] += dp[i][j]
    dp[i+1][j] += dp[i][j] * i

tot_num = sum(dp[-1])
boom_num = sum(dp[-1][:M+1])
tot_num, boom_num = gcd(tot_num, boom_num)
print('{}/{}'.format(boom_num, tot_num))
import sys
input = sys.stdin.readline

def init() :
  global n, k, coin_list
  n, k = map(int, input().split())
  coin_list = [int(input()) for _ in range(n)]

  return coin_list

def make_dp(coin_list) :
  dp = [0]*(k+1)
  dp[0] = 1
  
  for i in range(n) :
    for j in range(k+1) :
      if dp[j] > 0 and j + coin_list[i] <= k :
        dp[j + coin_list[i]] += dp[j]

  return dp

def solve() :
  coin_list = init()
  dp = make_dp(coin_list)
  print(dp[-1])

solve()
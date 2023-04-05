MAX = float('inf')

def init() :
  global N, K, checkpoint_list
  N, K = map(int, input().split())
  checkpoint_list = [list(map(int, input().split())) for _ in range(N)]

def cal_dist(a, b) :
  result = 0
  for i in range(2) :
    result += abs(checkpoint_list[a][i] - checkpoint_list[b][i])
  return result

def make_dp() :
  dp = [[MAX]*(K+1) for _ in range(N)]
  dp[0][-1] = 0

  for i in range(N-1) :
    for j in range(K+1) :
      if dp[i][j] == MAX :
        continue
      for k in range(j+1) :
        if i+k+1 >= N :
          break
        dp[i+k+1][j-k] = min(dp[i+k+1][j-k], dp[i][j] + cal_dist(i, i+k+1))

  return dp

def solve() :
  init()
  dp = make_dp()
  print(dp[-1][0])

solve()

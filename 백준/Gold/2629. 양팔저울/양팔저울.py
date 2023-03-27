def init() :
  N = int(input())
  weight_list = list(map(int, input().split()))
  M = int(input())
  target_weight = list(map(int, input().split()))
  return N, M, weight_list, target_weight


def make_weight_dp(N, weight_list) :
  dp = [[False]*40001 for _ in range(N)]

  dp[0][0] = dp[0][weight_list[0]] = True

  for i in range(N-1) :
    next_weight = weight_list[i+1]
    for j in range(40001) :
      if dp[i][j] :
        for k in [-1, 0, 1] :
          dp[i+1][abs(j + k*next_weight)] = True

  return dp

def is_enable_measure_weight(N, M, target_weight, dp) :
  result = list()
  for i in range(M) :
    flg = False
    for j in range(N) :
      if dp[j][target_weight[i]] :
        result.append('Y')
        flg = True
        break
    if not flg : 
      result.append('N')

  return result

def solve() :
  N, M, weight_list, target_weight = init()
  dp = make_weight_dp(N, weight_list)
  result = is_enable_measure_weight(N, M, target_weight, dp)
  print(*result)

solve()
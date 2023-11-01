import sys
input = sys.stdin.readline
MAX = float('inf')

def solve() :
  global N, W, enemy_list
  N, W = map(int, input().split())
  enemy_list = [list(map(int, input().split())) for _ in range(2)]

  flg = 0
  result = MAX
  result = min(result, cal_dp(0))
  for i in range(2) :
    if N > 1 and enemy_list[i][0] + enemy_list[i][-1] <= W :
      result = min(result, cal_dp(i+1))
      flg += 1

  if N > 2 and flg == 2 :
    result = min(result, cal_dp(3))
  print(result)

def dp_init(dp, mode = 0) :
  if mode not in [1, 3] :
    dp[0][1] = 1
  if mode not in [2, 3] :
    dp[0][0] = 1
  if mode == 0 and enemy_list[0][0] + enemy_list[1][0] <= W :
    dp[0][2] = 1
  else :
    dp[0][2] = 2

def dp_result(dp, mode = 0) :
  if mode == 0 :
    return dp[-1][2]
  elif mode in [1, 2] :
    return dp[-1][2-mode]
  else :
    return dp[-2][2]

def cal_dp(mode = 0) :
  dp = [[MAX]*3 for _ in range(N)]
  dp_init(dp, mode)

  for i in range(1, N) :
    flg = 0
    for j in range(2) :
      if enemy_list[j][i-1] + enemy_list[j][i] <= W :
        flg += 1
        dp[i][j] = min(dp[i][j], dp[i-1][1-j]+1)
      dp[i][j] = min(dp[i][j], dp[i-1][2]+1)
      dp[i][2] = min(dp[i][2], dp[i][j]+1)
    if enemy_list[0][i] + enemy_list[1][i] <= W :
      dp[i][2] = min(dp[i][2], dp[i-1][2]+1)
    if flg == 2 :
      if i > 1 :
        dp[i][2] = min(dp[i][2], dp[i-2][2]+2)
      elif mode == 0 :
        dp[i][2] = min(dp[i][2], 2)
  return dp_result(dp, mode)

for _ in range(int(input())) :
  solve()
import sys
input = sys.stdin.readline
px = [-1, -1, 0, 1]
py = [0, -1, -1, -1]
MAX = float('inf')
cnt = 1
while True :
  N = int(input())
  if N == 0 :
    break
  node_list = [list(map(int, input().split())) for _ in range(N)]
  
  dp = [[MAX]*3 for _ in range(N)]
  dp[0][1] = node_list[0][1]
  dp[0][2] = node_list[0][1] + node_list[0][2]
  
  for i in range(1, N) :
    for j in range(3) :
      min_val = MAX
      for k in range(4) :
        ai, aj = i+py[k], j+px[k]
        if -1 < aj < 3 and min_val > dp[ai][aj] :
          min_val = dp[ai][aj]
      dp[i][j] = node_list[i][j] + min_val
  
  print("{:d}. {:d}".format(cnt, dp[-1][1]))
  cnt += 1
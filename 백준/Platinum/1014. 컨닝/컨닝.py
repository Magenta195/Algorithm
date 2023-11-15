import sys
input = sys.stdin.readline

def solve() :
  N, M = map(int, input().split())

  maps = [input().strip() for _ in range(N)]
  dp = [[-1]*(1 << M) for _ in range(N)]

  for i in range(1 << M) :
    flg = True
    cnt = 0
    for j in range(M) :
      if not i & (1 << j) :
        continue
      if maps[0][j] == 'x' :
        flg = False
        break
      if j < M-1 and i & (1 << (j+1)) :
        flg = False
        break
      cnt += 1
    if flg :
      dp[0][i] = cnt

  for i in range(1, N) :
    for j in range(1 << M) :
      if dp[i-1][j] == -1 :
        continue
      for k in range(1 << M) :
        flg = True
        cnt = 0
        for l in range(M) :
          if not k & (1 << l) :
            continue
          if maps[i][l] == 'x' :
            flg = False
            break
          if l < M-1 and ((k & (1 << (l+1))) or (j & (1 << (l+1)))) :
            flg = False
            break
          if l > 0 and j & (1 << (l-1)) :
            flg = False
            break
          cnt += 1
        if flg :
          dp[i][k] = max(dp[i][k], dp[i-1][j] + cnt)

  print(max(max(map(max, dp)), 0))

for _ in range(int(input())) :
  solve()
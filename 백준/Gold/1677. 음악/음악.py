from re import A


Music1 = input().strip()
Music2 = input().strip()
Music3 = input().strip()

N, M, K = len(Music1), len(Music2), len(Music3)

if max(N, M, K) > min(N, M, K) * 2 + 1 :
  print(-1)
  exit()

def score(i, j, k) :
  _i = '&' if i % 2 == 0 else Music1[i // 2]
  _j = '&' if j % 2 == 0 else Music2[j // 2]
  _k = '&' if k % 2 == 0 else Music3[k // 2]

  if _i == _j == _k != '&':
    return 3
  if (_i == '&' and _j == _k != '&' or
      _j == '&' and _i == _k != '&' or
      _k == '&' and _i == _j != '&') :
    return 1
  return 0

dp = [[[-1]*(2*K+1) for _ in range(2*M+1)] for _ in range(2*N+1)]

for i in range(2) :
  for j in range(2) :
    for k in range(2) :
      dp[i][j][k] = score(i, j, k)

for i in range(1, 2*N+1) :
  for j in range(1, 2*M+1) :
    for k in range(1, 2*K+1) :
      for l in range(8) :
        _i, _j, _k = i - l//4 - 1, j - l%4//2 - 1, k - l%2 - 1
        if _i < 0 or _j < 0 or _k < 0 or dp[_i][_j][_k] == -1 :
          continue
        if _i % 2 == i % 2 == 0 or _j % 2 == j % 2 == 0 or _k % 2 == k % 2 == 0 :
          continue
        dp[i][j][k] = max(dp[i][j][k], dp[_i][_j][_k] + score(i, j, k))

ans = -1
for i in range(-2, 0) :
  for j in range(-2, 0) :
    for k in range(-2, 0) :
      ans = max(ans, dp[i][j][k])
print(ans)